%define		module			pygtksourceview
%define		pygtk_req		2:2.14.0
Summary:	GtkSourceView2 bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GtkSourceView2
Name:		python-gtksourceview2
Version:	2.10.1
Release:	8
License:	LGPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pygtksourceview/2.10/%{module}-%{version}.tar.bz2
# Source0-md5:	2654354d61422fb79d8375fc3a3b5393
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.7
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	gtksourceview2-devel >= 2.10.0
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.3.2
# for style.css
BuildRequires:	python-pygobject-apidocs >= 2.16.0
BuildRequires:	python-pygobject-devel >= 2.16.0
BuildRequires:	python-pygtk-devel >= %{pygtk_req}
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
Requires:	python-pygobject >= 2.16.0
Requires:	python-pygtk-gtk >= %{pygtk_req}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
GtkSourceView2 bindings for Python.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki GtkSourceView2.

%package devel
Summary:	GtkSourceView2 bindings for Python - development files
Summary(pl.UTF-8):	Pliki programistyczne wiązań Pythona do biblioteki GtkSourceView2
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	gtksourceview2-devel >= 2.10.0
Requires:	python-pygtk-devel >= %{pygtk_req}

%description devel
GtkSourceView2 bindings for Python - development files.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Pythona do biblioteki GtkSourceView2.

%package apidocs
Summary:	pygtksourceview2 API documentation
Summary(pl.UTF-8):	Dokumentacja API pygtksourceview2
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

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
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTMLdir=%{_gtkdocdir}/pygtksourceview2

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.la

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
