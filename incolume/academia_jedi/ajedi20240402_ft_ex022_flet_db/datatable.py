"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from flet import *
from myaction import conn

# ruff: noqa: A002, ANN001, ANN201, ARG001, ARG002, BLE001, C901, D101, D102, D103, D107, DTZ005, DTZ011, E501, ERA001, N802, N803, N806, PLR2004, S608, T201, TRY300

tb = DataTable(
    columns=[
        DataColumn(Text('actions')),
        DataColumn(Text('name')),
        DataColumn(Text('age')),
        DataColumn(Text('contact')),
        DataColumn(Text('email')),
        DataColumn(Text('address')),
        DataColumn(Text('gender')),
    ],
    rows=[],
)


def showdelete(e):
    try:
        myid = int(e.control.data)
        c = conn.cursor()
        c.execute('DELETE FROM users WHERE id=?', (myid,))
        conn.commit()
        print('success delete')
        tb.rows.clear()
        calldb()
        tb.update()

    except Exception as e:
        print(e)


id_edit = Text()
name_edit = TextField(label='name')
age_edit = TextField(label='age')
contact_edit = TextField(label='contact')
gender_edit = RadioGroup(
    content=Column([
        Radio(value='man', label='man'),
        Radio(value='woman', label='woman'),
    ]),
)
email_edit = TextField(label='email')
address_edit = TextField(label='address')


def hidedlg(e):
    dlg.visible = False
    dlg.update()


def updateandsave(e):
    try:
        myid = id_edit.value
        c = conn.cursor()
        c.execute(
            'UPDATE users SET name=?, contact=?, age=?,'
            ' gender=?, email=?, address=? WHERE id=?',
            (
                name_edit.value,
                contact_edit.value,
                age_edit.value,
                gender_edit.value,
                email_edit.value,
                address_edit.value,
                myid,
            ),
        )
        conn.commit()
        print('success Edit ')
        tb.rows.clear()
        calldb()
        dlg.visible = False
        dlg.update()
        tb.update()
    except Exception as e:
        print(e)


dlg = Container(
    # bgcolor='blue200',
    padding=10,
    content=Column([
        Row(
            [
                Text('Edit Form', size=30, weight='bold'),
                IconButton(icon='close', on_click=hidedlg),
            ],
            alignment='spaceBetween',
        ),
        name_edit,
        age_edit,
        contact_edit,
        Text('Select Gender', size=20, weight='bold'),
        gender_edit,
        email_edit,
        address_edit,
        ElevatedButton('Update', on_click=updateandsave),
    ]),
)


def showedit(e):
    data_edit = e.control.data
    id_edit.value = data_edit['id']
    name_edit.value = data_edit['name']
    age_edit.value = data_edit['age']
    contact_edit.value = data_edit['contact']
    gender_edit.value = data_edit['gender']
    email_edit.value = data_edit['email']
    address_edit.value = data_edit['address']

    dlg.visible = True
    dlg.update()


def calldb():
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    print(users)
    if users != '':
        keys = ['id', 'name', 'contact', 'age', 'gender', 'email', 'address']
        result = [dict(zip(keys, values, strict=False)) for values in users]
        for x in result:
            tb.rows.append(
                DataRow(
                    cells=[
                        DataCell(
                            Row([
                                IconButton(
                                    icon='create',
                                    icon_color='blue',
                                    data=x,
                                    on_click=showedit,
                                ),
                                IconButton(
                                    icon='delete',
                                    icon_color='red',
                                    data=x['id'],
                                    on_click=showdelete,
                                ),
                            ]),
                        ),
                        DataCell(Text(x['name'])),
                        DataCell(Text(x['age'])),
                        DataCell(Text(x['contact'])),
                        DataCell(Text(x['email'])),
                        DataCell(Text(x['address'])),
                        DataCell(Text(x['gender'])),
                    ],
                ),
            )


calldb()


dlg.visible = False
mytable = Column([dlg, Row([tb], scroll='always')])
