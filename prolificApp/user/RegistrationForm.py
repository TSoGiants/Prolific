from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,PasswordField,validators)
from wtforms.validators import DataRequired,Email,EqualTo