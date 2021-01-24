import tkinter.messagebox  # Importing TKINTER
from tkinter import END, DoubleVar
import mysql.connector  # Importing mysql connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="conn")  # connection establishing with Mysql connector
mycursor = mydb.cursor(buffered=True)


class StoreApp:  # new class storeapplication
    def __init__(self):  # define a function in Python
        self.product_i = None  # instance method
        self.main_window = tkinter.Tk()  # main window
        self.main_window.geometry("380x400+130+130")  # size of the window
        self.smart_mart_label = tkinter.Label(self.main_window, text="WELCOME TO SMART MART")  # display title for window
        self.smart_mart_label_lbl = tkinter.Label(self.main_window, text="\t\t")  # display title for window
        self.product_registration_button = tkinter.Button(self.main_window, text='Product Registration', width=30, height=3, command=self.__productRegistration)  # registration button
        self.individual_billing = tkinter.Button(self.main_window, text='Individual Billing', width=30, height=3, command=self.__individualBilling)  # individual billing button
        self.sales_report = tkinter.Button(self.main_window, text='Sales Report', width=30, height=3, command=self.__salesReport)  # sales report button
        self.product_shipping_details = tkinter.Button(self.main_window, text='Shipping Products to store', width=30, height=3, command=self.__productShipping)  # product shipping button
        self.stocking_report = tkinter.Button(self.main_window, text='Stocking Report', width=30, height=3, command=self.__stockReport)  # stocking report button
        self.smart_mart_label.pack() # smart mart label pack
        self.smart_mart_label_lbl.pack() # space label pack
        self.product_registration_button.pack()  # product registration pack
        self.individual_billing.pack()  # individual billing pack
        self.sales_report.pack()  # sales report pack
        self.product_shipping_details.pack()  # product shipping details packs
        self.stocking_report.pack()  # stocking report pack
        tkinter.mainloop()  # calling main loop

# ------------------------------------------------------------------------------------------------------------------------------------------
    def __productRegistration(self):  # define a function in Python
        self.product_registration_window = tkinter.Toplevel(self.main_window)  # Opening a new window
        self.product_registration_window.title = "Product Registration"  # display title for window
        self.product_registration_window.geometry("300x300+120+120")  # New window dimensions
        self.product_registration_label = tkinter.Label(self.product_registration_window, text='PRODUCT REGISTRATION')  # Initializing label
        self.product_registration_label.pack()  # Packing label
        self.product_number_label = tkinter.Label(self.product_registration_window, text='Product Number')  # Initializing label
        self.product_number_label.pack()  # Packing label
        self.product_number_input = tkinter.Entry(self.product_registration_window, width=20)  # Initializing input textbox
        self.product_number_input.pack()

        self.product_name_label = tkinter.Label(self.product_registration_window, text='Product Name')  # Initializing label
        self.product_name_label.pack()  # Packing label
        self.product_name_input = tkinter.Entry(self.product_registration_window, width=20)  # Initializing input textbox
        self.product_name_input.pack()

        self.product_description_label = tkinter.Label(self.product_registration_window, text='Product Description')  # Initializing label
        self.product_description_label.pack()  # Packing label
        self.product_description_input = tkinter.Entry(self.product_registration_window, width=20)  # Initializing input textbox
        self.product_description_input.pack()

        self.product_price_label = tkinter.Label(self.product_registration_window, text='Product Unit Price')  # Initializing label
        self.product_price_label.pack()  # Packing label
        self.product_price_input = tkinter.Entry(self.product_registration_window, width=20)  # Initializing input textbox
        self.product_price_input.pack()

        button_submit = tkinter.Button(self.product_registration_window, text="Save", width=20, command=self.submit)  # Button for saving all the data entered for product registration
        button_submit.pack()
        button_back = tkinter.Button(self.product_registration_window, text="Back", width=20, command=self.__back_registration)  # Button for going back to previous window
        button_back.pack()

    # submit button function
    def submit(self):  # define function
        sql = "INSERT INTO reg(product_number, product_name, product_description, product_unit_price) VALUES (%s, %s, %s, %s)"  # mysql insert value query for reg table
        val = (self.product_number_input.get(), self.product_name_input.get(), self.product_description_input.get(), self.product_price_input.get())  # get value from user
        mycursor.execute(sql, val)  # execute query
        mycursor.execute("DELETE FROM sales")  # execute delete query in sales table
        mycursor.execute("INSERT INTO sales (product_number,product_name,product_description, product_unit_price) SELECT * FROM reg")  # execute insert query for sales table,select query in reg table
        mydb.commit()
        self.product_number_input.delete(0, END)  # clear text in label after clicking event
        self.product_name_input.delete(0, END)  # clear text in label after clicking event
        self.product_description_input.delete(0, END)  # clear text in label after clicking event
        self.product_price_input.delete(0, END)  # clear text in label after clicking event

    def __back_registration(self):  # define a function in Python
        self.product_registration_window.destroy()  # close the window after click

    # -------------------------------------------------------------------------------------------------------------

    def __individualBilling(self):  # define a function in Python
        self.product_individual_billing_window = tkinter.Toplevel(self.main_window)  # Opening a new window
        self.product_individual_billing_window.title = "Individual Billing"  # display title for window
        self.product_individual_billing_window.geometry("300x300+120+120")  # New window dimensions
        self.product_individual_billing_label = tkinter.Label(self.product_individual_billing_window, text='INDIVIDUAL BILLING')  # Initializing label
        self.product_individual_billing_label.pack()  # Packing Label
        self.product_number_label = tkinter.Label(self.product_individual_billing_window, text='Product Number')  # Initializing label
        self.product_number_input_ib = tkinter.Entry(self.product_individual_billing_window, width=20)  # Initializing input textbox
        self.product_number_label.pack()  # Packing label 
        self.product_number_input_ib.pack()  # Packing input textbox
        self.product_unit_label = tkinter.Label(self.product_individual_billing_window, text='Number of units')  # Initializing label
        self.product_unit_input = tkinter.Entry(self.product_individual_billing_window, width=20)  # Initializing input textbox
        self.product_unit_label.pack()  # Packing label 
        self.product_unit_input.pack()  # Packing input textbox
        self.button_save = tkinter.Button(self.product_individual_billing_window, text="Generate Bill", width=20, command=self.__data_save_msg_individual_billing)  # Button for saving all the data entered
        self.button_back = tkinter.Button(self.product_individual_billing_window, text="Back", width=20, command=self.__back_individual_billing)  # Button for going back to previous window
        self.button_save.pack()  # Packing save button 
        self.button_back.pack()  # Packing Back Button

        # save button function

    def __data_save_msg_individual_billing(self):  # define a function in Python
        sql = "UPDATE sales set number_of_units = %s WHERE product_number = %s"  # mysql update query for sales table to find product_number
        val = (self.product_unit_input.get(), self.product_number_input_ib.get())  # value take it from user
        mycursor.execute(sql, val)  # execute query
        mydb.commit()
        sql = "UPDATE sales set total = product_unit_price * number_of_units"  # update query for  total in sales table
        mycursor.execute(sql)  # execute query
        mydb.commit()
        sql = "UPDATE sales set total_after_tax = total + (total * 13/100)"  # update query for total_after_tax in sales table
        mycursor.execute(sql)  # execute query
        mydb.commit()
        self.product_unit_input.delete(0, END)  # clear label text after clicking button
        self.product_number_input_ib.delete(0, END)  # clear label text after clicking button

    def __back_individual_billing(self):  # define a function in Python
        self.product_individual_billing_window.destroy()  # closing window

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    def __salesReport(self):  # define a function in Python
        self.sales_report_window = tkinter.Toplevel(self.main_window)  # Opening a new window
        canvas = tkinter.Canvas(self.sales_report_window, width=1080, height=400)  # canvas window height and width
        canvas.create_text(500, 10, text='SALES REPORT') # display the text using canvas widget
        canvas.pack()  # packing the canvas widget
        mycursor.execute("select * from sales")  # executing the query
        record = mycursor.fetchall()   # fetching the record from data base
        num = 60    # num used to display proper data
        canvas.create_text(400, num, text="\t\t\t\tproduct no\t\tproduct name\t\tdescription\t\tunit_price\t\tnumber_of_units\t\ttotal\t\ttotal_after_tax") # display line using the canvas text
        for x in record: # using for loop to fetch and display the data
            num += 15  # using the num increment to display the data position properly
            txt = "" + str(x[0]) + "\t\t\t" + str(x[1]) + "\t\t\t" + str(x[2]) + "\t\t\t" + str(x[3]) + "\t\t\t" + str(x[4]) + "\t\t\t" + str(x[5]) + "\t\t\t" + str(x[6])
            canvas.create_text(400, num, text=txt) # text by canvas widget
        quit_button = tkinter.Button(self.sales_report_window, text='QUIT', command=quit, width="20") # quit button on the window
        quit_button.pack()  # packing quit button

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------
    def __productShipping(self):  # define a function in Python
        self.product_shipping_details_window = tkinter.Toplevel(self.main_window)  # Opening a new window
        self.product_shipping_details_window.title = "Product Shipping"  # display title for window
        self.product_shipping_details_window.geometry("300x300+120+120")  # New window dimensions
        self.product_shipping_label = tkinter.Label(self.product_shipping_details_window, text='PRODUCT SHIPPING')  # Initializing label
        self.product_shipping_label.pack()  # Packing label

        self.product_number_label = tkinter.Label(self.product_shipping_details_window, text='Product Number')  # Initializing label
        self.product_number_label.pack()  # Packing label
        self.product_number_input_ship = tkinter.Entry(self.product_shipping_details_window, width=20)  # Initializing input textbox
        self.product_number_input_ship.pack()  # Packing input textbox

        self.product_unit_input_ship_lbl = tkinter.Label(self.product_shipping_details_window, text='Product Units shipped to the store')  # Initializing label
        self.product_unit_input_ship_lbl.pack()  # Packing label
        self.product_unit_input_ship_in = tkinter.Entry(self.product_shipping_details_window, width=20)  # Initializing input textbox
        self.product_unit_input_ship_in.pack()  # Packing input textbox

        self.product_wholesale_price_lbl = tkinter.Label(self.product_shipping_details_window, text='Product Wholesale Price')  # Initializing label
        self.product_wholesale_price_lbl.pack()  # Packing label and input textbox
        self.product_wholesale_price_in = tkinter.Entry(self.product_shipping_details_window, width=20)  # Initializing input textbox
        self.product_wholesale_price_in.pack()  # Packing input textbox

        self.product_expiry_date_lbl = tkinter.Label(self.product_shipping_details_window, text='Product Expiry date(if exists)')  # Initializing label
        self.product_expiry_date_lbl.pack()  # Packing input textbox
        self.product_expiry_date_in = tkinter.Entry(self.product_shipping_details_window, width=20)  # Initializing input textbox
        self.product_expiry_date_in.pack()  # Packing label and input textbox

        self.button_save = tkinter.Button(self.product_shipping_details_window, text="Save", width=20, height=2, command=self.__data_save_msg_shipping_detail)  # Button for saving all the data entered
        self.button_save.pack()  # Packing save button and back button
        self.button_back = tkinter.Button(self.product_shipping_details_window, text="Back", width=20, height=2, command=self.__back_shipping_detail)  # Button for going back to previous window
        self.button_back.pack()  # Packing Back Button

    # save button function
    def __data_save_msg_shipping_detail(self):  # define a function in Python
        sql = "INSERT INTO shipment(product_number, product_units_to_store, product_wholesale_price, product_ex_date) VALUES (%s, %s, %s, %s)"  # insert query for shipment table
        val = (self.product_number_input_ship.get(), self.product_unit_input_ship_in.get(), self.product_wholesale_price_in.get(), self.product_expiry_date_in.get())  # get value from the user
        mycursor.execute(sql, val)  # execute query
        mydb.commit()
        self.product_number_input_ship.delete(0, END)  # clear text after clicking button
        self.product_unit_input_ship_in.delete(0, END)  # clear text after clicking button
        self.product_wholesale_price_in.delete(0, END)  # clear text after clicking button
        self.product_expiry_date_in.delete(0, END)  # clear text after clicking button

    def __back_shipping_detail(self):  # define a function in Python
        self.product_shipping_details_window.destroy()  # closing window

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def __stockReport(self):  # define a function in Python
        self.stocking_report_window = tkinter.Toplevel(self.main_window)  # Opening a new window
        canvas = tkinter.Canvas(self.stocking_report_window, width=1080, height=400) # makes a new window width = 1080 , height = 400
        canvas.create_text(500, 10, text='STOCK REPORT')  # using X axis and Y axis the label is made
        canvas.pack() # packing the canvas text
        mycursor.execute("UPDATE shipment set status = 'ordered' WHERE product_units_to_store < '10'") # executing the query
        mycursor.execute("UPDATE shipment set status = 'not ordered' WHERE product_units_to_store > '10'") # executing the query
        mydb.commit()
        mycursor.execute("select * from shipment")  # executing the query
        record = mycursor.fetchall() #fetching the data from database
        num = 60  # num is axis used to display the proper data
        canvas.create_text(400, num, text="\t\tproduct_number\t\tproduct_units_to_store\t\tproduct_wholesale_price\t\tproduct_ex_date\t\tstatus") # to create the text line the canvas text is used
        for x in record: # using for loop to display the data
            num += 20   # x axis increment to display proper data
            txt = "" + str(x[0]) + "\t\t\t\t" + str(x[1]) + "\t\t\t" + str(x[2]) + "\t\t\t" + str(x[3] + "\t\t" + str(x[4])) # the display of data using the txt and forloop
            canvas.create_text(480, num, text=txt) # canvas text for data display
        quit_button = tkinter.Button(self.stocking_report_window, text='QUIT', command=quit, width="20")  # quit button
        quit_button.pack() # quit pack


StoreApp()
