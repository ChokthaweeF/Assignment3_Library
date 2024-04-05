from datetime import datetime, timedelta

class Member:
    def __init__(self, name, member_id, contact_info): #สร้างอ็อบเจกต์ของคลาส Member โดยกำหนดค่าเริ่มต้นกับข้อมูลพื้นฐานเกี่ยวกับสมาชิกของห้องสมุด

        self.name = name
        self.member_id = member_id
        self.contact_info = contact_info

class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def additional_info(self):#เมธอดใช้สำหรับการเพิ่มข้อมูลเพิ่มเติมเกี่ยวกับหนังสือ
        pass

class Book(Publication):
    def __init__(self, title, author, year, isbn, book_type): #สร้างอ็อบเจกต์ของคลาส Book โดยกำหนดค่าเริ่มต้นของแต่ละแอตทริบิวต์

        super().__init__(title, author, year)
        self.isbn = isbn
        self.book_type = book_type

    def additional_info(self):#คืนข้อมูลเพิ่มเติมของหนังสือ
        return f"ISBN: {self.isbn}, Type: {self.book_type}"

class Loan:
    def __init__(self, member, publication, borrow_date, due_date): #สร้างอ็อบเจกต์ของคลาส Loan เพื่อเก็บข้อมูลการยืมหนังสือ

        self.member = member
        self.publication = publication
        self.borrow_date = borrow_date
        self.due_date = due_date

class Library:
    def __init__(self): 
        self.members = [] #เก็บข้อมูลของสมาชิกทั้งหมดในห้องสมุด
        self.publications = [] #เก็บข้อมูลของหนังสือทั้งหมดในห้องสมุด
        self.loans = [] #เก็บข้อมูลการยืมหนังสือที่ทำไว้ในห้องสมุด

    def add_member(self, member): #เมธอดนี้ใช้สำหรับเพิ่มสมาชิกเข้าไปในรายชื่อสมาชิกของกลุ่ม
        self.members.append(member)

    def find_member(self, member_id): #ใช้ลูป for เพื่อวนลูปผ่านสมาชิกทุกตัวในลิสต์ self.members
        for member in self.members:  #ตรวจสอบว่า member_id ของสมาชิกในแต่ละรอบของลูปเท่ากับ member_id ที่เราต้องการค้นหาหรือไม่
            if member.member_id == member_id: #หากพบสมาชิกที่ตรงกับ member_id ที่เราต้องการค้นหา โค้ดจะคืนค่าสมาชิกนั้นออกมา
                return member  #หากไม่พบสมาชิกที่ตรงกับ member_id ที่เราต้องการค้นหา โค้ดจะคืนค่า None
        return None

    def display_member_details(self, member): #แสดงรายละเอียดของสมาชิกที่รับเข้ามา
        print(f"Name: {member.name}")
        print(f"Student ID: {member.member_id}")
        print(f"Phone Number: {member.contact_info}")

    def add_publication(self, publication): #เพิ่มข้อมูลการตีพิมพ์เข้าไปในรายการ
        self.publications.append(publication)

    def find_publication(self, title): #วนลูปผ่านรายการการตีพิมพ์ทั้งหมด
        for pub in self.publications: #ตรวจสอบว่าชื่อหนังสือของแต่ละรายการตรงกับชื่อที่ระบุหรือไม่
            if pub.title == title: #หากพบรายการการตีพิมพ์ที่ตรงกับชื่อที่ระบุ ให้คืนค่ารายการตีพิมพ์นั้น
                return pub
        return None  #ถ้าไม่พบรายการการตีพิมพ์ที่ตรงกับชื่อที่ระบุ ให้คืนค่า None

    def display_publication_details(self, publication): #แสดงรายละเอียดของการตีพิมพ์ที่ระบุ
        print(f"Title: {publication.title}")
        print(f"Author: {publication.author}")
        print(f"Year: {publication.year}")
        print(publication.additional_info())

    def borrow_publication(self, member, publication, borrow_date, due_date): #ตรวจสอบว่าการตีพิมพ์ที่ต้องการยืมอยู่ในรายการหรือไม่
        if publication in self.publications: #หากใช่ เพิ่มข้อมูลการยืมลงในรายการยืม
            self.loans.append(Loan(member, publication, borrow_date, due_date))
            return True
        else: #หากไม่ใช่ คืนค่า False เพื่อแสดงว่าไม่สามารถยืมได้
            return False

    def is_book_overdue(self, book): #วนลูปผ่านรายการยืมทั้งหมด
        for loan in self.loans: #ตรวจสอบว่าการตีพิมพ์ที่ถูกยืมในรายการยืมเป็นหนังสือที่เราต้องการตรวจสอบหรือไม่
            if loan.publication == book: #แปลงวันที่กำหนดส่งคืนของการยืมเป็นวัตถุ datetime
                due_date = datetime.strptime(loan.due_date, '%Y-%m-%d') # เปรียบเทียบว่าวันปัจจุบันมากกว่าวันที่กำหนดส่งคืนหรือไม่
                if datetime.now() > due_date:
                    return True
        return False

    def display_overdue_books(self): #สร้างรายการเพื่อเก็บหนังสือที่เกินกำหนด
        overdue_books = [] #วนลูปผ่านรายการยืมทั้งหมด
        for loan in self.loans: #แปลงวันที่กำหนดส่งคืนให้เป็นวัตถุ datetime
            due_date = datetime.strptime(loan.due_date, '%Y-%m-%d')  #ตรวจสอบว่าหนังสือเกินกำหนดหรือไม่
            if datetime.now() > due_date: #หากเกินกำหนด เพิ่มหนังสือลงในรายการหนังสือที่เกินกำหนด
                overdue_books.append(loan.publication)
        
        if overdue_books: #วนลูปผ่านหนังสือที่เกินกำหนด
            print("Overdue Books:") #ถ้ามีหนังสือที่เกินกำหนดโค้ดจะแสดงข้อความ หนังสือที่เกินกำหนด
            for book in overdue_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No overdue books found.")  #ถ้าไม่มีหนังสือที่เกินกำหนดโค้ดจะแสดงข้อความ ไม่พบหนังสือที่เกินกำหนด
            
    def display_loan_details(self, member):  #ค้นหารายการยืมทั้งหมดของสมาชิกที่กำหนด
        loans = [loan for loan in self.loans if loan.member == member]
        if loans:
            print("Trask Books:")
            for loan in loans: #วนลูปผ่านรายการยืมและแสดงรายละเอียด
                print(f"Publication: {loan.publication.title}")
                print(f"Borrow Date: {loan.borrow_date}")
                print(f"Due Date: {loan.due_date}")
        else:
            print("No Tasks Found For This Student.")

def add_new_member(library): #รับข้อมูลนักเรียนใหม่เข้าไปในห้องสมุด
    name = input("Enter Student's name: ")
    member_id = input("Enter Student ID: ")
    contact_info = input("Enter Phone Number: ")
    new_member = Member(name, member_id, contact_info)
    library.add_member(new_member)  #เพิ่มนักเรียนใหม่เข้าไปในห้องสมุด
    print("New Student Added Successfully.") #ข้อมูลนักเรียนใหม่เข้าไปในห้องสมุดเรียบร้อบแล้ว

def search_member(library): #รับรหัสนักเรียนที่ต้องการค้นหา
    member_id = input("Enter Student ID: ")  #ค้นหาข้อมูลของนักเรียนจากรหัสนักเรียนที่ระบุ
    member = library.find_member(member_id)
    if member:
        library.display_member_details(member) # แสดงรายละเอียดของนักเรียน
    else:
        print("Student not found.")

def add_new_book(library): #รับข้อมูลหนังสือใหม่
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter year of publication: ")
    isbn = input("Enter ISBN: ")
    book_type = input("Enter book type: ")
    new_book = Book(title, author, year, isbn, book_type) #เพิ่มหนังสือใหม่เข้าไปในห้องสมุด
    library.add_publication(new_book)
    print("New book added successfully.") #เพิ่มหนังสือใหม่เข้าห้องสมุดเรียบร้อยแล้ว

def search_book(library): #รับชื่อหนังสือที่ต้องการค้นหา
    title = input("Enter book title: ") #ค้นหาข้อมูลของหนังสือจากชื่อที่ระบุ
    book = library.find_publication(title)
    if book:
        library.display_publication_details(book)  #แสดงรายละเอียดของหนังสือ
    else:
        print("Book not found.")

def borrow_book(library): #รับรหัสสมาชิกที่ต้องการยืมหนังสือ
    member_id = input("Enter member ID: ") #ค้นหาข้อมูลของสมาชิกจากรหัสที่ระบุ
    member = library.find_member(member_id)
    if not member: #ถ้าไม่พบสมาชิก
        print("Member not found.") #แสดงข้อความว่า "ไม่พบสมาชิก" และสิ้นสุดการทำงานของเมธอด
        return

    title = input("Enter book title to borrow: ") #รับชื่อหนังสือที่ต้องการยืมจากผู้ใช้
    book = library.find_publication(title) #เมธอด find_publication ของห้องสมุดเพื่อค้นหาข้อมูลของหนังสือจากชื่อที่ระบุ
    if not book:
        print("Book not found.")
        return

    borrow_date = datetime.now().strftime('%Y-%m-%d') #ยืมหนังสือโดยกำหนดวันที่ยืมและกำหนดวันคืน
    due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')  # เพิ่มระยะเวลายืม 14 วัน
    if library.borrow_publication(member, book, borrow_date, due_date):
        print("Book borrowed successfully.")
    else:
        print("Book is not available for borrowing.")

def display_loan_details(library): #แสดงรายละเอียดของการยืมหนังสือโดยรับรหัสสมาชิกจากผู้ใช้
    member_id = input("Enter member ID: ") #ค้นหาข้อมูลของสมาชิกจากรหัสที่ระบุ
    member = library.find_member(member_id)
    if member:
        library.display_loan_details(member)  #แสดงรายละเอียดของการยืมของสมาชิก
    else:
        print("Member not found.")

def main(): #ฟังก์ชัน main() ดังกล่าวเป็นจุดเริ่มต้นของโปรแกรม โดยมีลักษณะเป็นการแสดงเมนูให้ผู้ใช้เลือกทำรายการต่าง ๆ 
    library = Library()
    while True:
        print("\n♦♦♦♦♦♦♦ WELCOME TO THE Mahalnw LIBRARY ♦♦♦♦♦♦♦\n")
        print("1. Add New Student")
        print("2. Search Student Data")
        print("3. Donate Book")
        print("4. Search Book")
        print("5. Borrow Book")
        print("6. Tasks Books")
        print("7. Overdue Books")  
        print("8. Exit")

        choice = input("Enter your choice: ")
        #ใช้สำหรับการดำเนินการตามที่ผู้ใช้ได้ทำเลือกในเมนู โดยเช็คค่า choice ที่ผู้ใช้ป้อนเข้ามา และดำเนินการตามเงื่อนไขต่าง ๆ
        if choice == '1':
            add_new_member(library)
        elif choice == '2':
            search_member(library)
        elif choice == '3':
            add_new_book(library)
        elif choice == '4':
            search_book(library)
        elif choice == '5':
            borrow_book(library)
        elif choice == '6':
            display_loan_details(library)
        elif choice == '7':
            library.display_overdue_books() 
        elif choice == '8':
            print("Exiting Program.")
            break
        else:
            print("Invalid Choice. Please Try Again.")


if __name__ == "__main__":
    main()