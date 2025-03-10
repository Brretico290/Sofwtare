import flet as ft


def main(page: ft.Page):
    page.title = "Contador de Clics"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    contador = ft.Text("Contador: 0", size=50)
    mensaje = ft.Text("", size=50, color=ft.Colors.BLUE)

    def actualizar_contador(e):
        valor = int(contador.value.split()[-1]) + 1
        contador.value = f"Contador: {valor}"
        mensajes = {1: "¡Has hecho tu primer clic!", 5: "¡Cinco clics! ¡Sigue así!",
                    10: "¡Diez clics! ¡Eres un experto!"}
        mensaje.value = mensajes.get(valor, "")
        contador.update()
        mensaje.update()

    def reiniciar_contador(e):
        contador.value = "Contador: 0"
        mensaje.value = ""
        contador.update()
        mensaje.update()

    page.add(
        ft.Column(
            [
                contador,
                mensaje,
                ft.ElevatedButton("Hacer clic", on_click=actualizar_contador),
                ft.ElevatedButton("Reiniciar", on_click=reiniciar_contador)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


ft.app(target=main)
#pase problemas para hacerlo pero me guie de las cosas simples de code examles para la base y despues fui generando ideas a ver si lo conseguia
# y este fue el resultado final 😁

