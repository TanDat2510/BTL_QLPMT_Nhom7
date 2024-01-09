import hashlib
from app import app,db
from app.models import Patient, Account, Books, Time, Medicine, MedicalForm, Prescription, Cashier
from flask_login import current_user



def add_booking(desc, date, time):
    b = Books(desc=desc, booked_date=date, time_id=time,patient=current_user)
    print('acb')
    db.session.add(b)
    db.session.commit()
    return b

def load_medicine_from():
    return  MedicalForm.query.all()

def load_booking():
    return Books.query.all()

def load_book():
    return Books.query.all()


def load_time():
    return Time.query.all()

def load_patient():
    return Patient.query.all()

def load_patientC(kw=None):
    patients = Patient.query
    if kw:
        patients = patients.filter(Patient.name.contains(kw))

    return patients.all()


def load_cashier():
    return Cashier.query.all()

def load_cash():
    return Cashier.query.all()



def load_medicine(kw=None):
    medicines = Medicine.query
    if kw:
        medicines = medicines.filter(Medicine.name.contains(kw))

    return medicines.all()

def load_medicalForm():
    return MedicalForm.query.all()

def load_prescription():
    return Prescription.query.all()



def get_user_by_id(user_id):
    return Account.query.get(user_id)


def auth_user(email, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return Account.query.filter(Account.email.__eq__(email.strip()),
                                Account.password.__eq__(password)).first()


def add_user(name, email, password, err_msg):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = Patient(name=name, email=email, password=password)
    db.session.add(u)
    db.session.commit()
    err_msg="Bạn đã đăng ký thành công"



def update_info(namSinh,sdt,diaChi,avatar,Patient_id, gioiTinh):
    p = Patient.query.filter_by(id=Patient_id).first()
    a = Account.query.filter_by(id=Patient_id).first()
    if p:
        p.namSinh = namSinh
        p.sdt = sdt
        p.diaChi = diaChi
        p.gioiTinh = gioiTinh
        db.session.commit()

def lenlichkham(id):
    b = Books.query.filter_by(id=id).first()
    b.lenLichKham = True
    db.session.commit()


# def sms(id):
#     # b = Books.query.filter_by(id=id).first()
#     # account_sid = 'AC190aec1c752f38726ac98a57ed1356b7'
#     # auth_token = 'a861de3ac30443372b918a9484c690b0'
#     # twilio_number = '+13035005221'
#     # my_phone = '+84374202752'
#     #
#     # client = Client(account_sid, auth_token)
#     #
#     # result = db.session.query(Books, Time) \
#     #     .join(Time, Books.time_id == Time.id).all()
#     #
#     # for books, time in result:
#     #     message_body = (
#     #         f"Xin chào bạn, đây là tin nhắn từ Phòng Mạch Tư ABC!\n"
#     #         f"Lịch khám của bạn là ngày {books.booked_date} lúc {time.period}\n"
#     #         "Địa chỉ: 123 Nguyễn Văn Cừ, Quận 1, TP.HCM\n"
#     #         "Lưu ý, bạn vui lòng đến trước 30 phút để làm thủ tục khám bệnh\n"
#     #         "Xin cảm ơn!"
#     #     )
#     #
#     # message = client.messages.create(
#     #     body=message_body,
#     #     from_=twilio_number,
#     #     to=my_phone
#     # )
#     # print(message.sid)
#     pass
# def lenphieukham(id):
#     b = Books.query.filter_by(id=id).first()
#     p = Patient.query.filter_by(id=b.patient_id).first()
   ## return p

def lenhoadon(id):
    medical_form = MedicalForm.query.get(1)
    patient = Patient.query.get(medical_form.patient_id)
    return patient.id