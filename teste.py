from flet import *

def main(page: Page):
    page.title = 'page home'

    def Loja(route):
        page.views.clear()
        page.views.append(
            View('/', [
                AppBar(title=Text('Cadastro'), bgcolor=colors.SURFACE_VARIANT),
                ElevatedButton('Loja', on_click=lambda _: page.go('/loja'))
            ])
        )
        if route == '/loja':
            page.views.append(
                View('/loja', [
                    AppBar(title=Text('Loja'), bgcolor=colors.GREEN),
                    ElevatedButton('Home', on_click=lambda _: page.go('/'))
                ])
            )

        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    page.on_route_change = Loja
    page.on_view_pop = view_pop

    # Set the initial route to home page
    page.go('/')

app(target=main, view=WEB_BROWSER)
