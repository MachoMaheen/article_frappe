# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from werkzeug.wrappers import Response


class Book(Document):
	pass

@frappe.whitelist(allow_guest=True)
def new_book():
	data = frappe.form_dict
	book = frappe.new_doc("Book")
	book.name = data.get("name")
	book.author = data.get("author")
	book.insert()

	return books_list()

@frappe.whitelist(allow_guest=True)
def delete_book(name):
    if frappe.db.exists("Book", name):
        frappe.delete_doc("Book", name)
        frappe.db.commit()
        return {"message": "Book deleted successfully"}
    else:
        frappe.throw("Book not found")
    # frappe.delete_doc_if_exists("Book",name)

@frappe.whitelist()
def books_list():
	books_list_html = frappe.render_template("templates/includes/book_list.html") 
	return Response(books_list_html)