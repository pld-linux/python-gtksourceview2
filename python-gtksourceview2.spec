%define		module			pygtksourceview
%define		pygtk_req		2:2.10.4
%define		gnome_python_req	2.18.0
#
Summary:	Gtksourceview2 bindings for Python
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki gtksourceview2
Name:		python-gtksourceview2
Version:	1.90.1
Release:	1
License:	GPL v2/LGPL v2.1 (see COPYING)
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/pygtksourceview/1.90/%{module}-%{version}.tar.bz2
# Source0-md5:	dcace16cfe05f7436c1c6c7f9b04f6fb
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	bug-buddy >= 2.16.0
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	gtksourceview2-devel >= 1.90.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	python-gnome-devel >= %{gnome_python_req}
BuildRequires:	python-pycairo-devel
BuildRequires:	python-pygtk-devel >= %{pygtk_req}
BuildRequires:	sed
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
Gtksourceview2 bindings for Python.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki gtksourceview2.

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

install -d $RPM_BUILD_ROOT%{_datadir}/doc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/{gtk-doc,doc}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/{{*.la,*.py},*/{*.la,*.py}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtksourceview2module.so
%{_gtkdocdir}/pygtksourceview2
%{_datadir}/pygtk/*/defs/gtksourceview2.defs
%{_pkgconfigdir}/*.pc
