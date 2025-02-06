"""Module."""


from flet import Page, SnackBar, app, transform
from incolume.academia_jedi.ajedi20240402_ft_ex022_flet_db.datatable import (
    calldb,
    mytable,
    tb,
)

# IMPORT YOU CREATE TABLE
from incolume.academia_jedi.ajedi20240402_ft_ex022_flet_db.myaction import (
    conn,
    create_table,
)

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

def main(page: Page):
    # AND RUN SCRIPT FOR CREATE TABLE WHEN FLET FIRST RUN
    create_table()

    page.scroll = 'auto'

    def showInput(e):
        inputcon.offset = transform.Offset(0, 0)
        page.update()

    def hidecon(e):
        inputcon.offset = transform.Offset(2, 0)
        page.update()

    def savedata(e):
        try:
            # INPUT TO DATABASE
            c = conn.cursor()
            c.execute(
                'INSERT INTO users (name,age,contact,email,address,gender)'
                ' VALUES(?,?,?,?,?,?)',
                (
                    name.value,
                    age.value,
                    contact.value,
                    email.value,
                    address.value,
                    gender.value,
                ),
            )
            conn.commit()
            print('success')

            # AND SLIDE RIGHT AGAIN IF FINAL INPUT SUUCESS
            inputcon.offset = transform.Offset(2, 0)

            # ADD SNACKBAR IF SUCCESS INPUT TO DATABASE

            page.snack_bar = SnackBar(Text('success INPUT'), bgcolor='green')

            page.snack_bar.open = True

            # REFRESH TABLE
            tb.rows.clear()
            calldb()
            tb.update()
            page.update()

        except Exception as e:
            print(e)

    # CREATE FIELD FOR INPUT

    name = TextField(label='name')
    age = TextField(label='age')
    contact = TextField(label='contact')
    email = TextField(label='email')
    address = TextField(label='address')
    gender = RadioGroup(
        content=Column([
            Radio(value='man', label='man'),
            Radio(value='woman', label='woman'),
        ]),
    )

    # CREATE MODAL INPUT FOR ADD NEW DATA
    inputcon = Card(
        # ADD SLIDE LEFT EFFECT
        offset=transform.Offset(2, 0),
        animate_offset=animation.Animation(600, curve='easeIn'),
        elevation=30,
        content=Container(
            content=Column([
                Row([
                    Text('Add new data', size=20, weight='bold'),
                    IconButton(icon='close', icon_size=30, on_click=hidecon),
                ]),
                name,
                age,
                contact,
                email,
                gender,
                address,
                FilledButton('save data', on_click=savedata),
            ]),
        ),
    )

    page.add(
        Column([
            Text('SCHOLL APP', size=30, weight='bold'),
            ElevatedButton('add new data', on_click=showInput),
            mytable,
            # AND DIALOG FOR ADD DATA
            inputcon,
            # NOTICE IF YOU ERROR
            # DISABLE import Datatable like this
        ]),
    )


if __name__ == '__main__':  # pragma: no cover
    app(target=main)
