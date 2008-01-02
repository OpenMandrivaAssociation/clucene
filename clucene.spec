%define major 0
%define libname %mklibname clucene %{major}
%define develname %mklibname clucene -d

Summary:	CLucene is a C++ port of Lucene
Name:		clucene
Version:	0.9.20
Release:	%mkrel 1
License:	LGPL
Group:		Archiving/Other
URL:            http://clucene.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/clucene/%{name}-core-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
CLucene is a C++ port of Lucene: the high-performance, full-featured 
text search engine written in Java. CLucene is faster than lucene 
as it is written in C++.

%package -n	%{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries
# Package not exists anymore
# Orifinal content was just test tools
Obsoletes: clucene <= 0.9.15

%description -n	%{libname}
CLucene is a C++ port of Lucene: the high-performance, full-featured 
text search engine written in Java. CLucene is faster than lucene 
as it is written in C++.

This package contains shared libraries for clucene.

%package -n	%{develname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C++
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%mklibname -d clucene 0

%description -n	%{develname}
CLucene is a C++ port of Lucene: the high-performance, full-featured 
text search engine written in Java. CLucene is faster than lucene 
as it is written in C++.

This package contains static libraries and development headers for 
clucene.

%prep

%setup -q -n %name-core-%version

%build
%configure2_5x

make

%install
rm -rf %{buildroot}

%makeinstall

# Provide a pointer to right place
ln -sf %{_libdir}/CLucene/clucene-config.h %buildroot/%_includedir/CLucene/

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,0755)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,0755)
%{_libdir}/CLucene/clucene-config.h
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a



