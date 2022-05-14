from py_calc_rpn.entrypoint.tui import factories


def main() -> int:
    app = factories.make_app()
    app.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
