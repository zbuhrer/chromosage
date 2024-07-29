# ./ui.py
import flet as ft


class UI:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Project Embeddings Generator and AI Assistant"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 20

        self.project_path = ft.Text()
        self.output_text = ft.Text(visible=False)
        self.query_input = ft.TextField(label="Ask about your project", visible=False)
        self.query_button = ft.ElevatedButton("Ask AI Assistant", visible=False)
        self.query_result = ft.Text(visible=False, selectable=True)
        self.chat_history = []

        self.dir_picker = ft.FilePicker(on_result=self.pick_directory)
        self.page.overlay.append(self.dir_picker)

        self.pick_dir_button = ft.ElevatedButton(
            "Select Project Directory",
            icon=ft.icons.FOLDER_OPEN,
            on_click=lambda _: self.dir_picker.get_directory_path()
        )

        self.show_chat_button = ft.ElevatedButton("Show/Hide Chat")

        self.page.add(
            ft.Column([
                ft.Text("ChromoSage Directory Assistant", size=24, weight=ft.FontWeight.BOLD),
                self.pick_dir_button,
                self.project_path,
                self.output_text,
                self.query_input,
                self.query_button,
                self.query_result,
                self.show_chat_button 
            ])
        )

    def pick_directory(self, e: ft.FilePickerResultEvent):
        if e.path:
            self.project_path.value = e.path
            self.process_project()
        self.page.update()

    def process_project(self):
        # overridden by the Controller
        pass

    def query_embeddings(self, e):
        # overridden by the Controller
        pass


class ChatWindow(ft.AlertDialog):
    def __init__(self, on_dismiss):
        super().__init__(
            modal=True,
            title=ft.Text("Chat Window"),
            on_dismiss=on_dismiss
        )

        self.content = ft.Column(
            width=500,
            height=400,
            scroll=ft.ScrollMode.AUTO
        )

        self.input_text = ft.TextField(hint_text="Type your message...", multiline=True)
        self.send_button = ft.ElevatedButton("Send", on_click=self.on_send)
        self.conversation_history = []

        self.content.controls.extend(
            [
                *self.conversation_history,
                ft.Divider(),
                self.input_text,
                ft.Row([self.send_button]),
            ]
        )

    def on_send(self, e):
        message = self.input_text.value
        if not message:
            return

        # Handle sending the message (you can implement this logic here)
        print(f"Received message: {message}")

        # Clear the input field and add the sent message to the conversation history
        self.input_text.value = ""
        self.conversation_history.append(ft.Text(message))
        self.update()