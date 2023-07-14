[1mdiff --git a/app2/__pycache__/__init__.cpython-311.pyc b/app2/__pycache__/__init__.cpython-311.pyc[m
[1mdeleted file mode 100644[m
[1mindex 89bd767..0000000[m
Binary files a/app2/__pycache__/__init__.cpython-311.pyc and /dev/null differ
[1mdiff --git a/app2/__pycache__/admin.cpython-311.pyc b/app2/__pycache__/admin.cpython-311.pyc[m
[1mdeleted file mode 100644[m
[1mindex ff4f67b..0000000[m
Binary files a/app2/__pycache__/admin.cpython-311.pyc and /dev/null differ
[1mdiff --git a/app2/__pycache__/apps.cpython-311.pyc b/app2/__pycache__/apps.cpython-311.pyc[m
[1mdeleted file mode 100644[m
[1mindex 76b1b95..0000000[m
Binary files a/app2/__pycache__/apps.cpython-311.pyc and /dev/null differ
[1mdiff --git a/app2/__pycache__/forms.cpython-311.pyc b/app2/__pycache__/forms.cpython-311.pyc[m
[1mdeleted file mode 100644[m
[1mindex 2805617..0000000[m
Binary files a/app2/__pycache__/forms.cpython-311.pyc and /dev/null differ
[1mdiff --git a/app2/__pycache__/formss.cpython-311.pyc b/app2/__pycache__/formss.cpython-311.pyc[m
[1mdeleted file mode 100644[m
[1mindex 0048a2a..0000000[m
Binary files a/app2/__pycache__/formss.cpython-311.pyc and /dev/null differ
[1mdiff --git a/app2/__pycache__/models.cpython-311.pyc b/app2/__pycache__/models.cpython-311.pyc[m
[1mdeleted file mode 100644[m
[1mindex e1f7ffb..0000000[m
Binary files a/app2/__pycache__/models.cpython-311.pyc and /dev/null differ
[1mdiff --git a/app2/__pycache__/views.cpython-311.pyc b/app2/__pycache__/views.cpython-311.pyc[m
[1mdeleted file mode 100644[m
[1mindex 07e3cfa..0000000[m
Binary files a/app2/__pycache__/views.cpython-311.pyc and /dev/null differ
[1mdiff --git a/app2/templates/base.html b/app2/templates/base.html[m
[1mindex c90bdd3..8868634 100644[m
[1m--- a/app2/templates/base.html[m
[1m+++ b/app2/templates/base.html[m
[36m@@ -44,3 +44,19 @@[m
 [m
     </body>[m
 </html>[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m[32m# http://127.0.0.1:8000/admin/[m
[32m+[m[32m# http://127.0.0.1:8000/home/[m
[32m+[m[32m# http://127.0.0.1:8000/show-books/[m
[32m+[m[32m# http://127.0.0.1:8000/show-single-book/[m
[32m+[m[32m# http://127.0.0.1:8000/add-book/[m
[32m+[m[32m# http://127.0.0.1:8000/edit-book/[m
[32m+[m[32m# http://127.0.0.1:8000/delete-book/[m
[32m+[m[32m# http://127.0.0.1:8000/soft_delete-book/[m
[32m+[m[32m# http://127.0.0.1:8000/form-view/[m
[1mdiff --git a/b99_library/urls.py b/b99_library/urls.py[m
[1mindex 5b7f163..3f73861 100644[m
[1m--- a/b99_library/urls.py[m
[1m+++ b/b99_library/urls.py[m
[36m@@ -41,13 +41,3 @@[m [murlpatterns = [[m
 [m
 [m
 [m
[31m-# http://127.0.0.1:8000/admin/[m
[31m-# http://127.0.0.1:8000/home/[m
[31m-# http://127.0.0.1:8000/show-books/[m
[31m-# http://127.0.0.1:8000/show-single-book/[m
[31m-# http://127.0.0.1:8000/add-book/[m
[31m-# http://127.0.0.1:8000/edit-book/[m
[31m-# http://127.0.0.1:8000/delete-book/[m
[31m-# http://127.0.0.1:8000/soft_delete-book/[m
[31m-# http://127.0.0.1:8000/form-view/[m
[31m-[m
