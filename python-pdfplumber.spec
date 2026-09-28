Name:		python-pdfplumber
Version:	0.11.10
Release:	1
Summary:	Plumb a PDF for detailed information about each char, rectangle, and line
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/pdfplumber/
Source0:	pdfplumber-0.11.10.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pdfminer.six)
BuildRequires:	python%{pyver}dist(pillow)
BuildArch:	noarch

%prep -a
# pypdfium2 ships prebuilt pdfium binaries. Text extraction uses pdfminer.
sed -i '/pypdfium2/d' requirements.txt
%description
Plumb a PDF for detailed information about each char, rectangle, and line.

%files
%{py_sitedir}/*
%{_bindir}/*
