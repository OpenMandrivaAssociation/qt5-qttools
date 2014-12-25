%define api 5
%define major %api

%define qtminor 4
%define qtsubminor 0

%define qtversion %{api}.%{qtminor}.%{qtsubminor}

%define qthelp %mklibname qt%{api}help %{major}
%define qthelpd %mklibname qt%{api}help -d

%define qtdesignercomponents %mklibname qt%{api}designercomponents %{major}
%define qtdesignercomponentsd %mklibname qt%{api}designercomponents -d

%define qtdesigner %mklibname qt%{api}designer %{major}
%define qtdesignerd %mklibname qt%{api}designer -d

%define qtclucene %mklibname qt%{api}clucene %{major}
%define qtclucened %mklibname qt%{api}clucene -d

%define _qt5_prefix %{_libdir}/qt%{api}
%define qttarballdir qttools-opensource-src-%{qtversion}

Name:		qt5-qttools
Version:	%{qtversion}
Release:	1
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt-project.org
Source0:	http://download.qt-project.org/official_releases/qt/%{api}.%{qtminor}/%{version}/submodules/%{qttarballdir}.tar.xz
Source1:	openmandriva-assistant-qt5.desktop
Source2:	openmandriva-designer-qt5.desktop
Source3:	openmandriva-linguist-qt5.desktop
Source100:	qt5-qttools.rpmlintrc
BuildRequires:	qt5-qtbase-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5DBus)

%description
Qt GUI tools

%files
%{_qt5_bindir}/lconvert
%{_qt5_bindir}/linguist
%{_qt5_bindir}/lrelease
%{_qt5_bindir}/lupdate
%{_qt5_bindir}/pixeltool
%{_qt5_bindir}/qtpaths
%{_qt5_bindir}/qtdiag
%{_qt5_datadir}/phrasebooks
%{_datadir}/applications/*linguist*.desktop
#FIXME: in the good package ?
%{_qt5_exampledir}/linguist

#------------------------------------------------------------------------------

%package	assistant
Summary:	Qt%{api} Assistant Doc Utility
Group:		Documentation
Requires:	qt5-qtbase-database-plugin-sqlite

%description	assistant
Qt Assistant provides a documentation Browser.

%files		assistant
%{_qt5_bindir}/assistant*
%{_qt5_bindir}/qcollectiongen*
%{_qt5_bindir}/qhelpconv*
%{_qt5_bindir}/qhelpgen*
%{_datadir}/applications/*assistant*.desktop
#FIXME: in the good package ?
%{_qt5_exampledir}/assistant

#------------------------------------------------------------------------------

%package	designer
Summary:	%{name} Visual Design Tool
Group:		Development/KDE and Qt

%description	designer
The Qt Designer is a visual design tool that makes designing and
implementing user interfaces a lot easier.

%files		designer
%{_qt5_bindir}/design*
%{_qt5_plugindir}/designer
%{_datadir}/applications/*designer*.desktop

#------------------------------------------------------------------------------

%package	qtdbus
Summary:	Qt%{api} Dbus Binary
Group:		Development/KDE and Qt

%description	qtdbus
Qt%{api} Dbus Binary.

The QtDBus module is a Unix-only library that you can use to perform 
Inter-Process Communication using the D-Bus protocol.

%files	qtdbus
%{_qt5_bindir}/qdbus
%{_qt5_bindir}/qdbusviewer

#------------------------------------------------------------------------------

%package -n %{qthelp}
Summary:	Qt%{api} Component Library
Group:		System/Libraries
Provides:	qthelplib = %{version}

%description -n %{qthelp}
Qt%{api} Component Library.

The QtHelp module provides classes for integrating online documentation
in applications.

%files -n %{qthelp}
%{_qt5_libdir}/libQt5Help.so.%{api}*

#------------------------------------------------------------------------------

%package -n	%{qthelpd}
Summary:	Devel files needed to build apps based on QtJsonDbCompat
Group:		Development/KDE and Qt
Requires:	%{qthelp} = %version
Requires:	%{name} = %version
Requires:	qt5-qtbase-devel = %version

%description -n %{qthelpd}
Devel files needed to build apps based on QtJsonDbCompat.

%files -n %{qthelpd}
%{_qt5_includedir}/QtHelp/
%{_qt5_libdir}/libQt%{api}Help.so
%{_qt5_libdir}/libQt%{api}Help.prl
%{_qt5_libdir}/cmake/Qt%{api}Help
%{_qt5_libdir}/pkgconfig/Qt%{api}Help.pc
%{_qt5_exampledir}/help/
%{_qt5_prefix}/mkspecs/modules/qt_lib_help.pri
%{_qt5_prefix}/mkspecs/modules/qt_lib_help_private.pri
#FIXME: Find a better place
%{_qt5_libdir}/cmake/Qt5LinguistTools/Qt5LinguistToolsConfig.cmake
%{_qt5_libdir}/cmake/Qt5LinguistTools/Qt5LinguistToolsMacros.cmake
%{_qt5_libdir}/cmake/Qt5LinguistTools/Qt5LinguistToolsConfigVersion.cmake
%if "%{_qt5_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Help.pc
%endif

#------------------------------------------------------------------------------

%package -n	%{qtclucene}
Summary:	Qt%{api} Component Library
Group:		System/Libraries
Provides:	qtclucenelib = %{version}

%description -n %{qtclucene}
Qt%{api} Component Library.

%files -n	%{qtclucene}
%{_qt5_libdir}/libQt%{api}CLucene.so.%{major}*
%if "%{_qt5_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}CLucene.so.%{major}*
%endif

#------------------------------------------------------------------------------

%package -n	%{qtclucened}
Summary:	Devel files needed to build apps based on QtCLucene
Group:		Development/KDE and Qt
Requires:	%{qtclucene} = %version

%description -n %{qtclucened}
Devel files needed to build apps based on QtCLucene.

%files -n %{qtclucened}
%{_qt5_includedir}/QtCLucene
%{_qt5_libdir}/libQt%{api}CLucene.so
%{_qt5_libdir}/libQt%{api}CLucene.prl
%{_qt5_libdir}/pkgconfig/Qt%{api}CLucene.pc
%{_qt5_prefix}/mkspecs/modules/qt_lib_clucene_private.pri
%if "%{_qt5_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}CLucene.pc
%endif

#------------------------------------------------------------------------------

%package -n	%{qtdesigner}
Summary:	Qt%{api} Component Library
Group:		System/Libraries
Provides:	qtdesignerlib = %{version}

%description -n %{qtdesigner}
Qt%{api} Component Library.

The QtDesigner module provides classes that allow you to create your own
custom widget plugins for Qt Designer, and classes that enable you to 
access Qt Designer's components.

%files -n %{qtdesigner}
%{_qt5_libdir}/libQt5Designer.so.%{api}*

#------------------------------------------------------------------------------

%package -n	%{qtdesignercomponents}
Summary:	Components for Qt Designer
Group:		System/Libraries

%description -n %{qtdesignercomponents}
Components for Qt Designer.

%files -n %{qtdesignercomponents}
%{_qt5_libdir}/libQt%{api}DesignerComponents.so.%{major}*
%if "%{_qt5_libdir}" != "%{_libdir}"
%{_libdir}/libQt%{api}DesignerComponents.so.%{major}*
%endif

#----------------------------------------------------------------------------

%package -n	%{qtdesignercomponentsd}
Summary:	Development files for Qt Designer Components
Group:		Development/KDE and Qt
Requires:	%{qtdesignercomponents} = %{EVRD}

%description -n %{qtdesignercomponentsd}
Development files for Qt Designer Components.

%files -n	%{qtdesignercomponentsd}
%{_qt5_includedir}/QtDesignerComponents
%{_qt5_libdir}/libQt%{api}DesignerComponents.so
%{_qt5_libdir}/libQt%{api}DesignerComponents.prl
%{_qt5_libdir}/pkgconfig/Qt%{api}DesignerComponents.pc
%if "%{_qt5_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}DesignerComponents.pc
%endif

%package -n	%{qtdesignerd}
Summary:	Devel files needed to build apps based on QtDesigner
Group:		Development/KDE and Qt
Requires:	%{qtdesigner} = %version

%description -n %{qtdesignerd}
Devel files needed to build apps based on QtDesigner.

%files -n	%{qtdesignerd}
%{_qt5_includedir}/QtDesigner
%{_qt5_libdir}/libQt%{api}Designer.so
%{_qt5_libdir}/libQt%{api}Designer.prl
%{_qt5_libdir}/cmake/Qt%{api}Designer
%{_qt5_libdir}/pkgconfig/Qt%{api}Designer.pc
%{_qt5_libdir}/pkgconfig/Qt5UiTools.pc
%{_qt5_exampledir}/designer
%{_qt5_exampledir}/uitools
%{_qt5_includedir}/QtUiTools
%{_qt5_libdir}/libQt5UiTools.prl
%{_qt5_libdir}/libQt5UiTools.a
%{_qt5_libdir}/cmake/Qt5UiTools
%{_qt5_prefix}/mkspecs/modules/qt_lib_designer.pri
%{_qt5_prefix}/mkspecs/modules/qt_lib_uitools.pri
%{_qt5_prefix}/mkspecs/modules/qt_lib_designer_private.pri
%{_qt5_prefix}/mkspecs/modules/qt_lib_designercomponents_private.pri
%{_qt5_prefix}/mkspecs/modules/qt_lib_uitools_private.pri
%if "%{_qt5_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Designer.pc
%endif

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir
%apply_patches

%build
%qmake_qt5

%make

#------------------------------------------------------------------------------

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}/%{_datadir}/applications
install -m 644 %SOURCE1 %{buildroot}/%{_datadir}/applications
install -m 644 %SOURCE2 %{buildroot}/%{_datadir}/applications
install -m 644 %SOURCE3 %{buildroot}/%{_datadir}/applications

sed -i -e 's#/usr/lib/qt5/bin#%{_qt5_bindir}#' %{buildroot}/%{_datadir}/applications/*.desktop

# Fix all buildroot paths
find %{buildroot}/%{_qt5_libdir} -type f -name '*prl' -exec perl -pi -e "s, -L%{_builddir}/\S+,,g" {} \;
find %{buildroot}/%{_qt5_libdir} -type f -name '*prl' -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" {} \;
find %{buildroot}/%{_qt5_libdir} -type f -name '*la' -print -exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;

# Don't reference builddir neither /usr(/X11R6)?/ in .pc files.
perl -pi -e '\
s@-L/usr/X11R6/%{_lib} @@g;\
s@-I/usr/X11R6/include @@g;\
s@-L/%{_builddir}\S+@@g'\
    `find . -name \*.pc`

# .la and .a files, die, die, die.
rm -f %{buildroot}%{_qt5_libdir}/lib*.la
