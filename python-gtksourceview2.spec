%define		module			pygtksourceview
%define		pygtk_req		2:2.10.4
%define		gnome_python_req	2.18.0
#
Summary:	Gtksourceview2 bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki gtksourceview2
Name:		python-gtksourceview2
Version:	1.90.3
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/pygtksourceview/1.90/%{module}-%{version}.tar.bz2
# Source0-md5:	a7f1c81c4637550a4bc2c3ee2a3182b7
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.7
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	gtksourceview2-devel >= 1.90.3
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.3.2
# for style.css
BuildRequires:	python-pygobject-apidocs >= 2.11.3
BuildRequires:	python-pygobject-devel >= 2.11.3
BuildRequires:	python-pygtk-devel >= %{pygtk_req}
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
Gtksourceview2 bindings for Python.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki gtksourceview2.

%package devel
Summary:	gtksourceview2 bindings for Python - development files
Summary(pl.UTF-8):	Pliki programistyczne wiązań Pythona do biblioteki gtksourceview2
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	gtksourceview2-devel >= 1.90.1
Requires:	python-pygtk-devel >= %{pygtk_req}

%description devel
gtksourceview2 bindings for Python - development files.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Pythona do biblioteki gtksourceview2.

%package apidocs
Summary:	pygtksourceview2 API documentation
Summary(pl.UTF-8):	Dokumentacja API pygtksourceview2
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
pygtksourceview2 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API pygtksourceview2.

%prep
%setup -q -n %{module}-%{version}

%build
sed -i 's/codegen\.py/codegen.pyc/' configure.ac
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTMLdir=%{_gtkdocdir}/pygtksourceview2

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{py_sitedir}/gtksourceview2.so

%files devel
%defattr(644,root,root,755)
%{pydefsdir}/gtksourceview2.defs
%{_pkgconfigdir}/pygtksourceview-2.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/pygtksourceview2
