"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from typing import Optional

from pydantic import BaseModel
from sqlalchemy.orm import Session

from .automation.run import run_automations
from .core import DBAutomation, DBItem, NotFoundError

# ruff: noqa: A002, ANN001, ANN201, ARG001, ARG002, BLE001, C901, D101, D102, D103, D107, DTZ005, DTZ011, E501, ERA001, N802, N803, N806, PLR2004, S608, T201, TRY300


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


def read_db_item(item_id: int, session: Session) -> DBItem:
    db_item = session.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        msg = f'Item with id {item_id} not found.'
        raise NotFoundError(msg)
    return db_item


def read_db_automations_for_item(
    item_id: int,
    session: Session,
) -> list[DBAutomation]:
    return (
        session.query(DBAutomation)
        .filter(DBAutomation.item_id == item_id)
        .all()
    )


def create_db_item(item: ItemCreate, session: Session) -> DBItem:
    db_item = DBItem(**item.model_dump(exclude_none=True))
    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


def update_db_item(item_id: int, item: ItemUpdate, session: Session) -> DBItem:
    db_item = read_db_item(item_id, session)
    for key, value in item.model_dump(exclude_none=True).items():
        setattr(db_item, key, value)
    session.commit()
    session.refresh(db_item)

    # get the automations
    automations = read_db_automations_for_item(db_item.id, session)
    run_automations(automations)

    return db_item


def delete_db_item(item_id: int, session: Session) -> DBItem:
    db_item = read_db_item(item_id, session)
    session.delete(db_item)
    session.commit()
    return db_item
