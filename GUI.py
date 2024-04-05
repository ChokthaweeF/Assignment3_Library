import PySimpleGUI as sg
from datetime import datetime, timedelta
from LIB import Library, Member, Book

# ฟังก์ชันสำหรับเพิ่มสมาชิกใหม่
def add_new_member_gui(library): #กำหนดโครงร่างของหน้าต่าง GUI
    layout = [
        [sg.Text('Enter Student\'s name: '), sg.InputText(key='-NAME-')],
        [sg.Text('Enter Student ID: '), sg.InputText(key='-ID-')],
        [sg.Text('Enter Phone Number: '), sg.InputText(key='-CONTACT-')],
        [sg.Button('Add Student'), sg.Button('Cancel')]
    ]
    window = sg.Window('Add New Student', layout) #สร้างหน้าต่าง GUI สำหรับเพิ่มนักเรียนใหม่
    while True:
        event, values = window.read() #รอรับเหตุการณ์และข้อมูลที่กรอกเข้ามาในหน้าต่าง GUI
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break #ออกจาก loop และจบการทำงานของโปรแกรม
        elif event == 'Add Student':
            name = values['-NAME-']
            member_id = values['-ID-']
            contact_info = values['-CONTACT-'] #สร้างอ็อบเจ็กต์ Member จากข้อมูลที่กรอก
            new_member = Member(name, member_id, contact_info) #สร้างอ็อบเจ็กต์ Member จากข้อมูลที่กรอก
            library.add_member(new_member)
            sg.popup("New Student Added Successfully.")  #แสดงข้อความยืนยันการเพิ่มนักเรียนใหม่
            break #ออกจาก loop และจบการทำงานของโปรแกรม
    window.close() #ปิดหน้าต่าง GUI หลังจากเสร็จสิ้นการทำงาน


# ฟังก์ชันสำหรับค้นหาสมาชิก
def search_member_gui(library):  #กำหนดโครงร่างของหน้าต่าง GUI
    layout = [
        [sg.Text('Enter Student ID: '), sg.InputText(key='-ID-')],
        [sg.Button('Search'), sg.Button('Cancel')]
    ]
    window = sg.Window('Search Student Data', layout) #สร้างหน้าต่าง GUI สำหรับค้นหาข้อมูลนักเรียน
    while True:
        event, values = window.read() #รอรับเหตุการณ์และข้อมูลที่กรอกเข้ามาในหน้าต่าง GUI
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break #ออกจาก loop และจบการทำงานของโปรแกรม
        elif event == 'Search':
            member_id = values['-ID-']
            member = library.find_member(member_id)  #เรียกใช้เมธอด find_member ในคลาส Library เพื่อค้นหาข้อมูลนักเรียน
            if member:
                sg.popup(f"Name: {member.name}\nMember ID: {member.member_id}\nContact Info: {member.contact_info}") #เมื่อพบข้อมูลของนักเรียนโปรแกรมจะแสดงข้อมูลของนักเรียนนั้นในหน้าต่าง Popup
            else:
                sg.popup("Member not found.")
            break #ออกจาก loop และจบการทำงานของโปรแกรม
    window.close() #โปรแกรมออกจากลูปและสิ้นสุดการทำงาน และปิดหน้าต่าง GUI ด้วยคำสั่ง window.close()

# ฟังก์ชันสำหรับเพิ่มหนังสือใหม่
def add_new_book_gui(library): #สร้างหน้าต่าง GUI โดยใช้โครงร่าง layout ที่กำหนด
    layout = [
        [sg.Text('Enter Book Title: '), sg.InputText(key='-TITLE-')],
        [sg.Text('Enter Author: '), sg.InputText(key='-AUTHOR-')],
        [sg.Text('Enter Year of Publication: '), sg.InputText(key='-YEAR-')],
        [sg.Text('Enter ISBN: '), sg.InputText(key='-ISBN-')],
        [sg.Text('Enter Book Type: '), sg.InputText(key='-TYPE-')],
        [sg.Button('Donate Book'), sg.Button('Cancel')]
    ]
    window = sg.Window('Donate Book', layout) #สร้างหน้าต่าง GUI สำหรับบริจาคหนังสือใหม่
    while True:
        event, values = window.read() #รอรับเหตุการณ์และข้อมูลที่กรอกเข้ามาในหน้าต่าง GUI
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break #ออกจาก loop และจบการทำงานของโปรแกรม
        elif event == 'Donate Book':
            title = values['-TITLE-'] #ดึงข้อมูลชื่อหนังสือที่ผู้ใช้กรอกเข้ามา
            author = values['-AUTHOR-']
            year = values['-YEAR-']
            isbn = values['-ISBN-']
            book_type = values['-TYPE-'] #ดึงข้อมูลประเภทหนังสือ
            new_book = Book(title, author, year, isbn, book_type) #สร้างอ็อบเจกต์ของหนังสือใหม่ด้วยข้อมูลที่ได้รับ
            library.add_publication(new_book)
            sg.popup("New Book Added Successfully.") #แสดงข้อความแจ้งเตือนว่าบันทึกข้อมูลหนังสือใหม่สำเร็จ
            break #ออกจาก loop และจบการทำงานของโปรแกรม
    window.close() #ปิดหน้าต่าง GUI หลังจากเสร็จสิ้นการทำงาน


# ฟังก์ชันสำหรับค้นหาหนังสือ
def search_book_gui(library): #กำหนดโครงร่างของหน้าต่าง GUI สำหรับค้นหาหนังสือ
    layout = [
        [sg.Text('Enter book title: '), sg.InputText(key='-TITLE-')],
        [sg.Button('Search'), sg.Button('Cancel')]
    ]
    window = sg.Window('Search Book', layout) #สร้างหน้าต่าง GUI สำหรับค้นหาหนังสือ 
    while True:
        event, values = window.read() #รอรับเหตุการณ์และข้อมูลที่ผู้ใช้กรอกเข้ามาในหน้าต่าง GUI
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break #ออกจาก loop และจบการทำงานของโปรแกรม
        elif event == 'Search':
            title = values['-TITLE-']
            book = library.find_publication(title)
            if book:
                sg.popup(f"Title: {book.title}\nAuthor: {book.author}\nYear: {book.year}\nISBN: {book.isbn}\nType: {book.book_type}")
            else:
                sg.popup("Book not found.")
            break #ออกจาก loop และจบการทำงานของโปรแกรม
    window.close() #ปิดหน้าต่าง GUI หลังจากเสร็จสิ้นการทำงาน

# ฟังก์ชันสำหรับยืมหนังสือ
def borrow_book_gui(library): #กำหนดโครงร่างของหน้าต่าง GUI สำหรับยืมหนังสือ
    layout = [ # สร้างหน้าต่าง GUI โดยใช้โครงร่าง layout ที่กำหนด
        [sg.Text('Enter member ID: '), sg.InputText(key='-ID-')],
        [sg.Text('Enter book title to borrow: '), sg.InputText(key='-TITLE-')],
        [sg.Button('Borrow Book'), sg.Button('Cancel')]
    ]
    window = sg.Window('Borrow Book', layout)
    while True:
        event, values = window.read() #รอรับเหตุการณ์และข้อมูลที่ผู้ใช้กรอกเข้ามาในหน้าต่าง GUI
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break #ออกจาก loop และจบการทำงานของโปรแกรม
        elif event == 'Borrow Book':
            member_id = values['-ID-'] #ดึงข้อมูลหมายเลขสมาชิกที่ผู้ใช้กรอกเข้ามา
            member = library.find_member(member_id) #ค้นหาข้อมูลสมาชิกในระบบโดยใช้เมธอด find_member ในคลาส Library
            if not member: # หากไม่พบข้อมูลสมาชิก
                sg.popup("Member not found.") #แสดงข้อความแจ้งเตือนว่าไม่พบข้อมูลสมาชิก
                break #ออกจาก loop และจบการทำงานของโปรแกรม
            title = values['-TITLE-']
            book = library.find_publication(title) #ค้นหาข้อมูลหนังสือในระบบโดยใช้เมธอด find_publication ในคลาส Library
            if not book: 
                sg.popup("Book not found.")
                break # ออกจาก loop และจบการทำงานของโปรแกรม
            borrow_date = datetime.now().strftime('%Y-%m-%d') #กำหนดวันที่ยืมเป็นวันปัจจุบันและแปลงเป็นรูปแบบ 'YYYY-MM-DD'
            due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d') #กำหนดวันที่กำหนดส่งคืนเป็น 14 วันหลังจากวันปัจจุบันและแปลงเป็นรูปแบบ 'YYYY-MM-DD'
            if library.borrow_publication(member, book, borrow_date, due_date): #ทำการยืมหนังสือด้วยเมธอด borrow_publication ในคลาส Library และตรวจสอบว่าเป็นไปด้วยความสำเร็จหรือไม่
                sg.popup("Book borrowed successfully.") 
            else:
                sg.popup("Book is not available for borrowing.")
            break #ออกจาก loop และจบการทำงานของโปรแกรม
    window.close()  #ปิดหน้าต่าง GUI หลังจากเสร็จสิ้นการทำงาน

# ฟังก์ชันสำหรับแสดงรายละเอียดการยืม
def display_loan_details_gui(library): #กำหนดโครงร่างของหน้าต่าง GUI สำหรับแสดงรายละเอียดการยืมหนังสือ
    layout = [
        [sg.Text('Enter member ID: '), sg.InputText(key='-ID-')],
        [sg.Button('Display Loan Details'), sg.Button('Cancel')]
    ]
    window = sg.Window('Display Loan Details', layout) #สร้างหน้าต่าง GUI โดยใช้โครงร่าง layout ที่กำหนด
    while True:
        event, values = window.read() #รอรับเหตุการณ์และข้อมูลที่ผู้ใช้กรอกเข้ามาในหน้าต่าง GUI
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break #ออกจาก loop และจบการทำงานของโปรแกรม
        elif event == 'Display Loan Details':
            member_id = values['-ID-'] #ดึงข้อมูลหมายเลขสมาชิกที่ผู้ใช้กรอกเข้ามา
            member = library.find_member(member_id) #ค้นหาข้อมูลสมาชิกในระบบโดยใช้เมธอด find_member ในคลาส Library
            if member: #ค้นหารายการยืมหนังสือทั้งหมดของสมาชิก
                loans = [loan for loan in library.loans if loan.member == member]
                if loans: #สร้างข้อความรายละเอียดการยืมหนังสือ
                    loan_details = '\n'.join([f"Publication: {loan.publication.title}\nBorrow Date: {loan.borrow_date}\nDue Date: {loan.due_date}" for loan in loans])
                    sg.popup("Loan Details:", loan_details) #แสดงข้อความรายละเอียดการยืมหนังสือ
                else:
                    sg.popup("No loans found for this member.") #แสดงข้อความว่าไม่พบการยืมหนังสือสำหรับสมาชิกนี้
            else:
                sg.popup("Member not found.") #แสดงข้อความแจ้งเตือนว่าไม่พบข้อมูลสมาชิก
            break #ออกจาก loop และจบการทำงานของโปรแกรม
    window.close() #ปิดหน้าต่าง GUI หลังจากเสร็จสิ้นการทำงาน

# ฟังก์ชันสำหรับแสดงหนังสือที่เลยกำหนดคืน
def display_overdue_books_gui(library): #ค้นหาหนังสือที่มีกำหนดส่งคืนผ่านวันที่ปัจจุบัน
    overdue_books = [loan.publication for loan in library.loans if datetime.strptime(loan.due_date, '%Y-%m-%d') < datetime.now()]
    if overdue_books: #สร้างรายการหนังสือที่เกินกำหนดส่งคืนเป็นข้อความ
        book_list = '\n'.join([f"- {book.title} by {book.author}" for book in overdue_books])
        sg.popup("Overdue Books:", book_list) #แสดงข้อความรายการหนังสือที่เกินกำหนดส่งคืน
    else:
        sg.popup("No overdue books found.") #แสดงข้อความว่าไม่มีหนังสือที่เกินกำหนดส่งคืน

# ฟังก์ชันสำหรับระบบหลัก
def main(): 
    sg.theme('LightBlue1') #กำหนดธีมของ GUI

    layout = [
    [sg.Text('Mahalnw LIBRARY', font=('Helvetica', 20),pad=((75, 0)))],
    [sg.Column(layout=[[sg.Button('Add New Student', size=(20, 2),pad=((100, 0)))]])],
    [sg.Column(layout=[[sg.Button('Search Student Data', size=(20, 2),pad=((100, 0)))]])],
    [sg.Column(layout=[[sg.Button('Donate Book', size=(20, 2),pad=((100, 0)))]])],
    [sg.Column(layout=[[sg.Button('Search Book', size=(20, 2),pad=((100, 0)))]])],
    [sg.Column(layout=[[sg.Button('Borrow Book', size=(20, 2),pad=((100, 0)))]])],
    [sg.Column(layout=[[sg.Button('Tasks Books', size=(20, 2),pad=((100, 0)))]])],
    [sg.Column(layout=[[sg.Button('Overdue Books', size=(20, 2),pad=((100, 0)))]])],
    [sg.Column(layout=[[sg.Button('Exit', size=(20, 2),pad=((100, 0)))]])],
]



    window = sg.Window('Mahalnw LIBRARY', layout) #สร้างหน้าต่าง GUI ของโปรแกรมที่มีชื่อว่า "Mahalnw LIBRARY"

    library = Library() #สร้างอ็อบเจกต์ของคลาส Library

    while True: #รอรับเหตุการณ์จากผู้ใช้ผ่านหน้าต่าง GUI
        event, _ = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':  #ถ้าปุ่มปิดหน้าต่างถูกคลิกหรือผู้ใช้ปิดหน้าต่าง GUI
            break
        elif event == 'Add New Student': 
            add_new_member_gui(library) # เรียกใช้ฟังก์ชันเพื่อเพิ่มสมาชิกใหม่
        elif event == 'Search Student Data': 
            search_member_gui(library)  #เรียกใช้ฟังก์ชันเพื่อผู้ใช้ค้นหาข้อมูลสมาชิกในห้องสมุด
        elif event == 'Donate Book':
            add_new_book_gui(library) #เรียกใช้ฟังก์ชันเพื่อให้ผู้ใช้บริจาคหนังสือใหม่เข้าสู่ห้องสมุด
        elif event == 'Search Book': 
            search_book_gui(library) #เรียกใช้ฟังก์ชันเพื่อให้ผู้ใช้ค้นหาข้อมูลหนังสือในห้องสมุด
        elif event == 'Borrow Book':
            borrow_book_gui(library) #เรียกใช้ฟังก์ชันเพื่อให้ผู้ใช้ยืมหนังสือจากห้องสมุด
        elif event == 'Tasks Books':
            display_loan_details_gui(library)  #เรียกใช้ฟังก์ชันเพื่อแสดงรายละเอียดของการยืมหนังสือทั้งหมด
        elif event == 'Overdue Books':
            display_overdue_books_gui(library) #เรียกใช้ฟังก์ชันเพื่อแสดงรายชื่อหนังสือที่เกินกำหนดคืน
    window.close()

if __name__ == "__main__":
    main()