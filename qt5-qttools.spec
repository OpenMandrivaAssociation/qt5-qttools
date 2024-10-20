%define api %(echo %version |cut -d. -f1)
%define major %api
%define beta %{nil}

%define qthelp %mklibname qt%{api}help %{major}
%define qthelpd %mklibname qt%{api}help -d

%define qtdesignercomponents %mklibname qt%{api}designercomponents %{major}
%define qtdesignercomponentsd %mklibname qt%{api}designercomponents -d

%define qtdesigner %mklibname qt%{api}designer %{major}
%define qtdesignerd %mklibname qt%{api}designer -d

%define qtclucene %mklibname qt%{api}clucene %{major}
%define qtclucened %mklibname qt%{api}clucene -d

%define _qt5_prefix %{_libdir}/qt%{api}

Name:		qt5-qttools
Version:	5.15.15
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qttools-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qttools-everywhere-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		https://www.qt.io
Source1:	openmandriva-assistant-qt5.desktop
Source2:	openmandriva-designer-qt5.desktop
Source3:	openmandriva-linguist-qt5.desktop
Source100:	qt5-qttools.rpmlintrc
Patch1:		lrelease-zlib.patch
Patch2:		fix_qtdesigner_include_paths.patch
Patch3:		qttools-5.12.1-clang-7.0.patch
Patch4:		qttools-compilefix-if-qtwebkit-is-enabled.patch
Patch5:		qdoc-compile.patch
# From KDE
Patch1001:	0001-Ensure-FileAttributeSetTable-is-filled-ordered-so-we.patch
Patch1002:	0002-Drop-superfluous-network-dependency-from-assistant-h.patch
Patch1003:	0003-qdoc-Ensure-the-generated-temporary-header-file-is-c.patch
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5WebView)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	qt5-qtqml-private-devel
BuildRequires:	qt5-qtquick-private-devel
BuildRequires:	qt5-qtqmlmodels-private-devel
BuildRequires:	clang-devel llvm-devel
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1
# For scaling *.desktop icons
BuildRequires:	imagemagick

%description
Qt tools.

%files
%{_qt5_bindir}/pixeltool
%{_qt5_bindir}/qdistancefieldgenerator
%{_qt5_bindir}/qtpaths
%{_qt5_bindir}/qtdiag
%{_qt5_bindir}/qtplugininfo
%{_qt5_bindir}/qtattributionsscanner
%{_qt5_bindir}/qcollectiongenerator
%{_bindir}/pixeltool
%{_bindir}/qdistancefieldgenerator
%{_bindir}/qtpaths
%{_bindir}/qtdiag
%{_bindir}/qtplugininfo
%{_bindir}/qtattributionsscanner
%{_bindir}/qcollectiongenerator

#----------------------------------------------------------------------------

%package -n qdoc%{api}
Summary:	Qt documentation generator, version 5
Group:		Development/KDE and Qt

%description -n qdoc%{api}
Qt documentation generator, version 5.

%files -n qdoc%{api}
%{_qt5_bindir}/qdoc
%{_bindir}/qdoc
%{_libdir}/cmake/Qt5AttributionsScannerTools
%{_libdir}/cmake/Qt5DocTools

#------------------------------------------------------------------------------

%package -n	qt%{api}-assistant
Summary:	Qt%{api} Assistant Doc Utility
Group:		Documentation
Requires:	qt5-qtbase-database-plugin-sqlite

%description -n	qt%{api}-assistant
Qt Assistant provides a documentation Browser.

%files -n qt%{api}-assistant
%{_qt5_bindir}/assistant*
%{_qt5_bindir}/qhelpgen*
%{_bindir}/assistant*
%{_bindir}/qhelpgen*
%{_datadir}/applications/*assistant*.desktop
%{_datadir}/icons/hicolor/*/apps/assistant.*
#FIXME: in the good package ?
%{_qt5_exampledir}/assistant

#------------------------------------------------------------------------------

%package -n	qt%{api}-designer
Summary:	%{name} Visual Design Tool
Group:		Development/KDE and Qt

%description -n	qt%{api}-designer
The Qt Designer is a visual design tool that makes designing and
implementing user interfaces a lot easier.

%files	-n	qt%{api}-designer
%{_qt5_bindir}/design*
%{_bindir}/design*
%{_qt5_plugindir}/designer
%{_datadir}/applications/*designer*.desktop
%{_datadir}/icons/hicolor/*/apps/QtProject-designer.*

#------------------------------------------------------------------------------

%package -n	qt%{api}-linguist
Summary:	%{name} Visual Design Tool
Group:		Development/KDE and Qt

%description -n	qt%{api}-linguist
Translation tool for Qt based applications

%files	-n	qt%{api}-linguist
%{_qt5_datadir}/phrasebooks
%{_datadir}/applications/*linguist*.desktop
%{_datadir}/icons/hicolor/*/apps/linguist.*
#FIXME: in the good package ?
%{_qt5_exampledir}/linguist

#------------------------------------------------------------------------------
%package -n	qt%{api}-linguist-tools
Summary:	%{name} Visual Design Tool
Group:		Development/KDE and Qt
Provides:	qt5-linguist-tools = %{EVRD}
Requires:	qt%{api}-linguist = %{EVRD}

%description -n	qt%{api}-linguist-tools
Translation tool for Qt based applications

%files	-n	qt%{api}-linguist-tools
%{_qt5_bindir}/lconvert
%{_qt5_bindir}/lprodump
%{_qt5_bindir}/lrelease
%{_qt5_bindir}/lrelease-pro
%{_qt5_bindir}/lupdate
%{_qt5_bindir}/lupdate-pro
%{_qt5_bindir}/linguist*
%{_bindir}/lconvert
%{_bindir}/lprodump
%{_bindir}/lrelease
%{_bindir}/lrelease-pro
%{_bindir}/lupdate
%{_bindir}/lupdate-pro
%{_bindir}/linguist*
#FIXME: Find a better place
%{_qt5_libdir}/cmake/Qt5LinguistTools/Qt5LinguistToolsConfig.cmake
%{_qt5_libdir}/cmake/Qt5LinguistTools/Qt5LinguistToolsMacros.cmake
%{_qt5_libdir}/cmake/Qt5LinguistTools/Qt5LinguistToolsConfigVersion.cmake
#------------------------------------------------------------------------------

%package	qtdbus
Summary:	Qt%{api} Dbus Binary
Group:		Development/KDE and Qt

%description qtdbus
Qt%{api} Dbus Binary.

The QtDBus module is a Unix-only library that you can use to perform 
Inter-Process Communication using the D-Bus protocol.

%files qtdbus
%{_qt5_bindir}/qdbus
%{_qt5_bindir}/qdbusviewer
%{_bindir}/qdbus
%{_bindir}/qdbusviewer

#------------------------------------------------------------------------------

%package -n %{qthelp}
Summary:	Qt%{api} Component Library
Group:		System/Libraries
Provides:	qthelplib = %{EVRD}

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
Requires:	%{qthelp} = %{EVRD}
Requires:	%{name} = %{EVRD}

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
%if "%{_qt5_libdir}" != "%{_libdir}"
%{_libdir}/pkgconfig/Qt%{api}Help.pc
%endif


#------------------------------------------------------------------------------

%package -n	%{qtdesigner}
Summary:	Qt%{api} Component Library
Group:		System/Libraries

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
%{_libdir}/cmake/Qt5DesignerComponents

%package -n	%{qtdesignerd}
Summary:	Devel files needed to build apps based on QtDesigner
Group:		Development/KDE and Qt
Requires:	%{qtdesigner} = %{EVRD}
Requires:	qt%{api}-designer = %{EVRD}

%description -n %{qtdesignerd}
Devel files needed to build apps based on QtDesigner.

%files -n	%{qtdesignerd}
#FIXME: find better place
%{_qt5_includedir}/QtUiPlugin
%{_qt5_libdir}/cmake/Qt5UiPlugin/Qt5UiPluginConfig.cmake
%{_qt5_libdir}/cmake/Qt5UiPlugin/Qt5UiPluginConfigVersion.cmake
%{_qt5_prefix}/mkspecs/modules/qt_lib_uiplugin.pri
%{_libdir}/libQt5UiPlugin.prl
%{_libdir}/pkgconfig/Qt5UiPlugin.pc
#
%{_qt5_includedir}/QtDesigner
%{_qt5_libdir}/libQt%{api}Designer.so
%{_qt5_libdir}/libQt%{api}Designer.prl
%{_qt5_libdir}/cmake/Qt%{api}Designer
%{_qt5_libdir}/pkgconfig/Qt%{api}Designer.pc
%{_qt5_libdir}/pkgconfig/Qt5UiTools.pc
%{_qt5_exampledir}/designer
%{_qt5_exampledir}/uitools
%{_qt5_includedir}/QtUiTools
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
%autosetup -n %(echo %qttarballdir |sed -e 's,-opensource,,') -p1
%{_qt5_prefix}/bin/syncqt.pl -version %{version}

# thermonuclear hack
# use it or investigate what's wrong with
# *** No rule to make target '../../../../shared/qtpropertybrowser/qtpropertybrowserutils.cpp',
# needed by '.obj/qtpropertybrowserutils.o'.
# hint: path too long, should be ../../../shared/qtpropertybrowser/qtpropertybrowserutils.cpp
%ifarch %{armx} %{x86_64} %{ix86}
ln -sf src/shared/ shared
%endif

%build
%qmake_qt5
%make_build

# uitools is a static library -- putting LLVM bytecode in there
# wreaks havoc for anything trying to link to it without using lto
# (or even using gcc)
# Let's rebuild it without lto...
rm lib/libQt5UiTools.a
sed -i -e 's,-flto=thin,,g' src/designer/src/uitools/Makefile
cd src/designer/src/uitools
make clean
%make_build

#------------------------------------------------------------------------------

%install
%make_install INSTALL_ROOT=%{buildroot}

# Make the menus great again...
mkdir -p %{buildroot}/%{_datadir}/applications
install -m 644 %SOURCE1 %{buildroot}/%{_datadir}/applications
install -m 644 %SOURCE2 %{buildroot}/%{_datadir}/applications
install -m 644 %SOURCE3 %{buildroot}/%{_datadir}/applications
for i in 32 48 64 128; do
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
	convert -scale ${i}x${i} src/designer/src/designer/images/designer.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/QtProject-designer.png
	convert -scale ${i}x${i} src/assistant/assistant/images/assistant-128.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/assistant.png
	convert -scale ${i}x${i} src/linguist/linguist/images/icons/linguist-128-32.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/linguist.png
done

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

# Fix reference to non-existing pkgconfig module
sed -i -e 's,Qt5UiPlugin,Qt5UiTools,g' %{buildroot}%{_libdir}/pkgconfig/Qt5Designer.pc

# The .prl file breaks building kjsembed because it changes Qt library paths
# to $QTDIR/lib instead of plain old libdir
# There's no point in prl files anyway, so let's dump it...
rm -f %{buildroot}%{_libdir}/libQt5UiTools.prl

# Make sure scripts can find the tools
mkdir -p %{buildroot}%{_bindir}
cd %{buildroot}%{_qt5_bindir}
for i in *; do
	ln -s %{_qt5_bindir}/$i %{buildroot}%{_bindir}/
done
