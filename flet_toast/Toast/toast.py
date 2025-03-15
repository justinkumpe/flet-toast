"""FletToast - Crie toasts personalizados usando a biblioteca flet do python."""

from ..deprecated import deprecated
from ..Controls.controls import Toast
from ..Controls.controls import ft
from ..Types.types import Position


class FletToast:
    """
    Crie toasts personalizados usando a biblioteca flet do python.

    ---
    Consulte a documentação pelo site: https://pypi.org/project/flet-toast/
    """

    def success(
        self,
        page: ft.Page,
        message: str,
        position: Position = Position.TOP_RIGHT,
        duration: int = 3,
        color: ft.Colors = ft.Colors.BLUE,
    ) -> Toast:
        """
        Display a success toast message.

        Args:
            page (ft.Page): The page where the toast will be displayed.
            message (str): The message to be displayed in the toast.
            position (Position, optional): The position of the toast on the page. Defaults to Position.TOP_RIGHT.
            duration (int, optional): The duration the toast will be visible in seconds. Defaults to 3.
            color (ft.Colors, optional): The color of the toast. Defaults to ft.Colors.BLUE.

        Returns:
            Toast: The created toast object.
        """
        toast = Toast(
            page=page,
            color=color,
            text=message,
            icon=ft.Icons.CHECK_CIRCLE_OUTLINED,
            position=position,
            duration=duration,
        )

        return toast

    @deprecated("Use method success")
    def sucess(
        self,
        page: ft.Page,
        message: str,
        position: Position = Position.TOP_RIGHT,
        duration: int = 3,
    ) -> Toast:
        """
        Alias for the success method. This method is deprecated.

        Args:
            page (ft.Page): The page where the toast will be displayed.
            message (str): The message to be displayed in the toast.
            position (Position, optional): The position of the toast on the page. Defaults to Position.TOP_RIGHT.
            duration (int, optional): The duration the toast will be visible in seconds. Defaults to 3.

        Returns:
            Toast: The created toast object.
        """
        return self.success(page, message, position, duration)  # Alias

    def warning(
        self,
        page: ft.Page,
        message: str,
        position: Position = Position.TOP_RIGHT,
        duration: int = 3,
        color: ft.Colors = ft.Colors.PURPLE,
    ) -> Toast:
        """
        Display a warning toast message.

        Args:
            page (ft.Page): The page where the toast will be displayed.
            message (str): The message to be displayed in the toast.
            position (Position, optional): The position of the toast on the page. Defaults to Position.TOP_RIGHT.
            duration (int, optional): The duration the toast will be visible in seconds. Defaults to 3.
            color (ft.Colors, optional): The color of the toast. Defaults to ft.Colors.PURPLE.

        Returns:
            Toast: The created toast object.
        """
        toast = Toast(
            page=page,
            color=color,
            text=message,
            icon=ft.Icons.WARNING_ROUNDED,
            position=position,
            duration=duration,
        )

        return toast

    def error(
        self,
        page: ft.Page,
        message: str,
        position: Position = Position.TOP_RIGHT,
        duration: int = 3,
        color: ft.Colors = ft.Colors.RED,
    ) -> Toast:
        """
        Display an error toast message.

        Args:
            page (ft.Page): The page where the toast will be displayed.
            message (str): The message to be displayed in the toast.
            position (Position, optional): The position of the toast on the page. Defaults to Position.TOP_RIGHT.
            duration (int, optional): The duration the toast will be visible in seconds. Defaults to 3.
            color (ft.Colors, optional): The color of the toast. Defaults to ft.Colors.RED.

        Returns:
            Toast: The created toast object.
        """
        toast = Toast(
            page=page,
            color=color,
            text=message,
            icon=ft.Icons.ERROR,
            position=position,
            duration=duration,
        )

        return toast


flet_toast = FletToast()
