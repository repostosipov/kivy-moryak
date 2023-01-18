from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem, ThreeLineListItem, ThreeLineAvatarListItem, OneLineAvatarIconListItem
from kivy.core.window import Window
from kivymd.uix.list import ImageLeftWidget
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton, MDRectangleFlatIconButton

import requests

r = requests.get('https://moryak.site/api/adverts/')
data_vak = r.json()

r = requests.get('https://moryak.site/api/companys/')
data_company = r.json()

r = requests.get('https://moryak.site/api/ships/')
data_flot = r.json()

Window.size = (500, 800)

KV = '''
<ItemConfirm>
    on_release: root.set_icon(check)

    CheckboxLeftWidget:
        id: check
        group: "check"

MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightblue"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Вакансии'
            icon: 'ship-wheel'
     
            MDScrollView:
                MDList:
                    id: container
        



        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Компании'
            icon: 'domain'

            MDScrollView:
                MDList:
                    id: container2

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Флот'
            icon: 'ferry'

            MDScrollView:
                MDList:
                    id: container3
'''


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False


class Test(MDApp):
    dialog = None

    def build(self):
        self.title = 'Моряк Инфо'
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def on_start(self):
        '''СЛАВА'''
        # for item in data_vak:
        #     self.root.ids.container.add_widget(
        #         ThreeLineAvatarListItem(
        #             text=f"{item['name']}",
        #             secondary_text=f"Должность: {item['position']}",
        #             tertiary_text= f"{item['salary']} ₽",
        #         )
        #     )
        for item in data_vak:
            items = ThreeLineAvatarListItem(
                text=f"{item['name']}",
                secondary_text=f"Должность: {item['position']}",
                tertiary_text=f"{item['salary']} ₽",
            )
            image = ImageLeftWidget(source='logo.png')
            items.add_widget(image)
            self.root.ids.container.add_widget(items)

        for item in data_company:
            self.root.ids.container2.add_widget(
                ThreeLineAvatarListItem(
                    text=f"{item['name']}",
                    secondary_text=f"Телефон: {item['tel']}",
                    tertiary_text=f"{item['des']}",
                )
            )
        for item in data_flot:
            self.root.ids.container3.add_widget(
                ThreeLineAvatarListItem(
                    text=f"{item['name']}",
                    secondary_text=f"Компания: {item['company']}",
                    tertiary_text=f"{item['country']}",
                )
            )

    def show_confirmation_dialog(self):
        '''МОДАЛЬНОЕ ОКНО ФИЛЬТРА ВАКАНСИЙ'''
        if not self.dialog:
            self.dialog = MDDialog(
                title="Phone ringtone",
                type="confirmation",
                items=[
                    ItemConfirm(text="Callisto"),
                    ItemConfirm(text="Luna"),
                    ItemConfirm(text="Night"),
                    ItemConfirm(text="Solo"),
                    ItemConfirm(text="Phobos"),
                    ItemConfirm(text="Diamond"),
                    ItemConfirm(text="Sirena"),
                    ItemConfirm(text="Red music"),
                    ItemConfirm(text="Allergio"),
                    ItemConfirm(text="Magic"),
                    ItemConfirm(text="Tic-tac"),
                ],
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()


Test().run()
