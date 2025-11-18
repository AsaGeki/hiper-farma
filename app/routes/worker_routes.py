from flask import Blueprint, render_template, request, redirect, flash
from app.models.worker_model import WorkerModel

workers = Blueprint("workers", __name__)

@workers.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        cpf = request.form.get("cpf")

        if not first_name or not last_name or not cpf:
            flash("Todos os campos são obrigatórios.")
            return redirect("/workers/create")

        WorkerModel.create(first_name, last_name, cpf)
        return redirect("/workers/list")

    return render_template("worker_create.html")


@workers.route("/list")
def list_workers():
    workers = WorkerModel.list_all()
    return render_template("worker_list.html", workers=workers)
