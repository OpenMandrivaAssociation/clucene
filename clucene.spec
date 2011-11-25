%define develname %mklibname clucene -d
# Do not push for the moment

Summary:	C++ port of Lucene
Name:		clucene
Version:	2.3.3.4
Release:	%mkrel 0
License:	LGPL
Group:		Archiving/Other
URL:            http://clucene.sourceforge.net/
BuildRequires:	cmake
BuildRequires:  zlib-devel
Source0:	http://prdownloads.sourceforge.net/clucene/%{name}-core-%{version}.tar.gz


%description
CLucene is a C++ port of Lucene: the high-performance, full-featured 
text search engine written in Java. CLucene is faster than lucene 
as it is written in C++.

#------------------------------------------------------------------------------
%define clucene_core_major 2
%define libclucene_core %mklibname clucene-core %{clucene_core_major} 

%package -n	%libclucene_core
Summary:	Shared libraries for %{name}
Group:		System/Libraries

%description -n %libclucene_core
CLucene is a C++ port of Lucene: the high-performance, full-featured 
text search engine written in Java. CLucene is faster than lucene 
as it is written in C++.

This package contains shared libraries for clucene.

%files -n %libclucene_core

%_libdir/libclucene-core.so.*

#------------------------------------------------------------------------------

%define clucene_shared_major 2
%define libclucene_shared %mklibname clucene_shared %{clucene_shared_major}


%package -n     %libclucene_shared
Summary:        Shared libraries for %{name}
Group:          System/Libraries

%description -n %libclucene_shared
CLucene is a C++ port of Lucene: the high-performance, full-featured
text search engine written in Java. CLucene is faster than lucene
as it is written in C++.

This package contains shared libraries for clucene.

%files -n %libclucene_shared

%_libdir/libclucene-shared.so.*

#------------------------------------------------------------------------------

%package -n	%{develname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C++
Provides:	%{name}-devel = %version-%release
Provides:	lib%{name}-devel = %version-%release
Requires:	%libclucene_shared = %version-%release
Requires:       %libclucene_core = %version-%release

%description -n	%{develname}
CLucene is a C++ port of Lucene: the high-performance, full-featured 
text search engine written in Java. CLucene is faster than lucene 
as it is written in C++.

This package contains static libraries and development headers for 
clucene.

%files -n %{develname}

%{_includedir}/CLucene.h
%{_includedir}/CLucene/
%_libdir/pkgconfig/libclucene-core.pc
%_libdir/CLuceneConfig.cmake/CLuceneConfig.cmake
%_libdir/libclucene-shared.so
%_libdir/libclucene-core.so

#------------------------------------------------------------------------------


%prep

%setup -q -n %name-core-%version

%build
%cmake

%make

%install

%makeinstall_std -C build  

