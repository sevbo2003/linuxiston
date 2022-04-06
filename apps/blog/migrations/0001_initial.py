# Generated by Django 4.0.3 on 2022-04-05 11:06

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=50)),
                ("avatar", models.ImageField(upload_to="author-avatars")),
                ("bio", models.CharField(max_length=300)),
                ("telegram", models.URLField()),
                ("instagram", models.URLField()),
                ("youtube", models.URLField()),
                ("github", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Faq",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                ("description", models.CharField(max_length=1000)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Faq",
                "verbose_name_plural": "FAQ",
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name": "tag",
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.CreateModel(
            name="VideoPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("video_url", models.URLField()),
                ("description", models.CharField(max_length=300)),
                ("body", ckeditor.fields.RichTextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("thumbnail", models.ImageField(upload_to="post-thumbnails")),
                ("slug", models.SlugField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.author"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="blog.category"
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True, related_name="vlikes", to=settings.AUTH_USER_MODEL
                    ),
                ),
                ("tags", models.ManyToManyField(to="blog.tag")),
            ],
            options={
                "verbose_name": "Video post",
                "verbose_name_plural": "Video blog posts",
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="VideoComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.CharField(max_length=500)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video_comments",
                        to="blog.videopost",
                    ),
                ),
            ],
            options={
                "verbose_name": "video comment",
                "verbose_name_plural": "Video Comments",
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=300)),
                ("body", ckeditor.fields.RichTextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("thumbnail", models.ImageField(upload_to="post-thumbnails")),
                ("slug", models.SlugField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.author"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="blog.category"
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
                    ),
                ),
                ("tags", models.ManyToManyField(to="blog.tag")),
            ],
            options={
                "verbose_name": "post",
                "verbose_name_plural": "Blog posts",
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.CharField(max_length=500)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.post",
                    ),
                ),
            ],
            options={
                "verbose_name": "comment",
                "verbose_name_plural": "Comments",
                "ordering": ("-created",),
            },
        ),
    ]
