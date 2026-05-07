import argparse
import uvicorn
from data.init_db import init_database


def main():
    parser = argparse.ArgumentParser(description="BestChange API")
    subparsers = parser.add_subparsers(dest="command", help="Команды")

    run_parser = subparsers.add_parser("run", help="Запустить сервер")
    run_parser.add_argument("--host", default="127.0.0.1")
    run_parser.add_argument("--port", type=int, default=8000)
    run_parser.add_argument("--reload", action="store_true")

    subparsers.add_parser("init-db", help="Инициализировать базу данных")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "run":
        uvicorn.run("main:app", host=args.host, port=args.port, reload=args.reload)

    elif args.command == "init-db":
        init_database()


if __name__ == "__main__":
    main()