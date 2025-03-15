[![es](https://img.shields.io/badge/lang-es-yellow.svg)](README.es.md)

# Toastfy - Toast Notification Library for Flet

`Toastfy` is a powerful and flexible library that allows the creation and display of "toast" notifications in Flet applications. With `Toastfy`, you can easily add success, error, and warning toasts to your applications, customizing the position and behavior of the notifications.

## Features

- **Success, Error, and Warning Toasts**: Specific notifications for different scenarios.
- **Customizable Positioning**: Choose from several predefined positions on the screen.
- **Simple Integration**: Easy to integrate and use in any Flet application.

![Different toasts generated](https://raw.githubusercontent.com/webtechmoz/flet-toast/master/assets/flet_toast.png)

## Installation

To install the `Toastfy` library, run:

```bash
pip install flet_toast
```
## Usage Example

Below is a simple example of how to use the Toastfy class in a Flet application:
```python
import flet as ft
from flet_toast import flet_toast

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    
    control = ft.Row(
        controls=[
            ft.ElevatedButton(
                text='Success',
                color=ft.colors.BLUE,
                on_click=lambda e: clicked_success(e)
            ),
            ft.ElevatedButton(
                text='Warning',
                color=ft.colors.PURPLE,
                on_click=lambda e: clicked_warning(e)
            ),
            ft.ElevatedButton(
                text='Error',
                color=ft.colors.RED,
                on_click=lambda e: clicked_error(e)
            )
        ]
    )

    def clicked_success(e):
        flet_toast.success(
            page=page,
            message='Success',
            position=flet_toast.Position.TOP_RIGHT,
            duration=5
        )
    
    def clicked_warning(e):
        flet_toast.warning(
            page=page,
            message='Warning',
            position=flet_toast.Position.BOTTOM_RIGHT,
            duration=5
        )
    
    def clicked_error(e):
        flet_toast.error(
            page=page,
            message='Error',
            position=flet_toast.Position.BOTTOM_LEFT,
            duration=5
        )

    page.add(control)

if __name__ == '__main__':
    ft.app(target=main)
```

## Documentation

### Methods
**success**:
Displays a success toast notification.

- `page`: The Flet page where the toast will be displayed.
- `message`: The message to be displayed in the toast.
- `position`: The position of the toast on the screen.
- `duration`: The duration of the toast notification.

**error**:
Displays an error toast notification.

- `page`: The Flet page where the toast will be displayed.
- `message`: The message to be displayed in the toast.
- `position`: The position of the toast on the screen.
- `duration`: The duration of the toast notification.

**warning**:
Displays a warning toast notification.

- `page`: The Flet page where the toast will be displayed.
- `message`: The message to be displayed in the toast.
- `position`: The position of the toast on the screen.
- `duration`: The duration of the toast notification.

### Properties
**position**:
Defines the possible positions to display toast notifications on the screen. The options include:

- `top_left`: Top left corner.
- `top_right`: Top right corner.
- `bottom_left`: Bottom left corner.
- `bottom_right`: Bottom right corner (default).

**duration**:
Defines the time the toast notification will be visible on the screen. This should be an integer.

## What's New in 0.6.0
- Adjustment of toasts for version 0.25.1 of Flet.

## What's New in 0.5.0
- Grouping of visible toasts.

## What's New in 0.4.2
- Bug fix when the toast is started asynchronously.

## What's New in 0.4.0
- Toasts are now generated asynchronously so as not to block the normal execution of the program.

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for more details.

## Contributions
Contributions are welcome! Feel free to open issues and pull requests on the GitHub repository.