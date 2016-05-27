__author__ = "Travis Wilson"

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

from GUI import TravisWilsonA1

item_catalogue = TravisWilsonA1.loading_items()

class Store_GUI(App):

    def __init__(self, **kwargs):
        super(Store_GUI, self).__init__(**kwargs)
        self.item_catalogue = item_catalogue
        self.in_items = []

    def build(self):
        self.title = "Button Event Demo"
        self.root = Builder.load_file('TravisWilsonA2.kv')
        self.load_items()
        return self.root

    def load_items(self):
        for items in item_catalogue:
            del items[4]
            temp_button = Button(text=items[0], on_press = self.hire_items)
            temp_button.bind(on_press= self.item_label_change)
            self.root.ids.itemBox.add_widget(temp_button)


    def add_item_button(self, button):
        self.popup_note = "Please enter the details of the new items"
        self.root.ids.popup.open()

    def press_save(self, item_name, item_detail, item_price):
        item_name = self.root.ids.itemName.text
        item_detail = self.root.ids.itemDetail.text
        item_price = self.root.ids.itemPrice.text
        item_avail = "in"

        temp_item_list = []
        temp_item_list.append(item_name)
        temp_item_list.append(item_detail)
        temp_item_list.append(item_price)
        temp_item_list.append(item_avail)
        item_catalogue.append(temp_item_list)

        temp_button = Button(text=item_name, id = "item_button", on_press = self.hire_items)
        temp_button.bind(on_release=self.item_label_change)
        self.root.ids.itemBox.add_widget(temp_button)

        print(item_catalogue)

        self.root.ids.popup.dismiss()
        self.clear_fields()

    def clear_fields(self):
        self.root.ids.itemName.text = ""
        self.root.ids.itemDetail.text = ""
        self.root.ids.itemPrice.text = ""

    def press_cancel(self):
        self.root.ids.popup.dismiss()
        self.clear_fields()

    def item_label_change(self, button):
        self.root.ids.item_detail_label.text = "{}".format(button.text)

    def hire_items(self, button):
        if self.root.ids.hire_button.state == 'down':
            print("button down1")
            if button.state == 'down':
                print("button down2")
                if button.text not in self.in_items:
                    self.in_items.append(button.text)
                    print(self.in_items)
                elif button.text in self.in_items:
                    self.root.ids.item_detail_label.text = 'Item already hired'
                else:
                    self.root.ids.item_detail_label.text = 'Click to hire'
        elif button.state == 'up':
            self.in_items.remove("Hire Item/s")
        else:
            pass

        for items in self.in_items:
            if items in self.item_catalogue[:]:
                items[3] = "userHired"
                print(items)

        print(item_catalogue)

    def checkout_items(self, button):
        TravisWilsonA1.write_to_csv(item_catalogue)
        App.get_running_app().stop()


Store_GUI().run()



