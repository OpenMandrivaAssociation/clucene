%define date 20111220
%define major	2
%define devname	%mklibname %{name} -d

Summary:	C++ port of Lucene
Name:		clucene
Version:	2.3.3.4
Release:	%mkrel -c %{date} 4
License:	LGPL
Group:		Archiving/Other
Url:            http://clucene.sourceforge.net/
# Zé: we are using git, so to generate the source file we run:
# git archive --prefix=clucene-2.3.3.4/ master | xz > clucene-2.3.3.4.tar.xz
#Source0:	http://prdownloads.sourceforge.net/clucene/%{name}-core-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.xz
# include LUCENE_SYS_INCLUDES in pkgconfig --cflags output
# imported fedora patch
Patch0:		clucene-core-2.3.3.4-pkgconfig_sys_includes.patch
Patch1:		clucene-2.3.3.4-fix-major.patch
Patch2:		patch-clucene-2.3.3.4-install-contribs-lib.diff
BuildRequires:	cmake
BuildRequires:	pkgconfig(zlib)

%description
CLucene is a C++ port of Lucene: the high-performance, full-featured 
text search engine written in Java. CLucene is faster than lucene 
as it is written in C++.

#------------------------------------------------------------------------------
%define libclucene_core %mklibname clucene-core %{major} 
%package -n	%{libclucene_core}
Summary:	Shared libraries for %{name}
Group:		System/Libraries
%rename		%{_lib}clucene_core2
Provides:	clucene-core2 

%description -n %{libclucene_core}
CLucene is a C++ port of Lucene: the high-performance, full-featured 
text search engine written in Java. CLucene is faster than lucene 
as it is written in C++.

This package contains shared libraries for clucene.

%files -n %{libclucene_core}
%{_libdir}/libclucene-core.so.%{major}*

#------------------------------------------------------------------------------
%define libclucene_shared %mklibname clucene_shared %{major}
%package -n	%{libclucene_shared}
Summary:	Shared libraries for %{name}
Group:		System/Libraries

%description -n %{libclucene_shared}
CLucene is a C++ port of Lucene: the high-performance, full-featured
text search engine written in Java. CLucene is faster than lucene
as it is written in C++.

This package contains shared libraries for clucene.

%files -n %{libclucene_shared}
%{_libdir}/libclucene-shared.so.%{major}*

#------------------------------------------------------------------------------
%define contrib %mklibname clucene-contribs-lib %{major}
%package -n	%contrib
Summary:	Language specific text analyzers for %{name}
Group:		System/Libraries
Requires:	%libclucene_core = %{version}-%{release}

%description -n %contrib
Language specific text analyzers for %{name}

%files -n %contrib
%_libdir/libclucene-contribs-lib.so.%{major}*

#------------------------------------------------------------------------------
%package -n	%{devname}
Summary:	Development library and header files for the %{name} library
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libclucene_shared} = %{version}-%{release}
Requires:       %{libclucene_core} = %{version}-%{release}
# Zé: we need to add this provides to avoid break upgrade
%ifnarch x86_64
Provides:	devel(libclucene)
%else
Provides:	devel(libclucene(64bit))
%endif

%description -n	%{devname}
CLucene is a C++ port of Lucene: the high-performance, full-featured 
text search engine written in Java. CLucene is faster than lucene 
as it is written in C++.

This package contains development libraries and development headers for 
clucene.

%files -n %{devname}
%{_includedir}/CLucene.h
%{_includedir}/CLucene/
%{_libdir}/pkgconfig/libclucene-core.pc
%{_libdir}/CLuceneConfig.cmake/CLuceneConfig.cmake
%{_libdir}/lib*.so

#------------------------------------------------------------------------------
%prep
%setup -q
%apply_patches

%build
%cmake \
	-DBUILD_CONTRIBS_LIB:BOOL=ON
%make

%install
%makeinstall_std -C build

