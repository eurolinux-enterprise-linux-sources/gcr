%ifarch %{ix86} x86_64 ppc ppc64 ppc64le s390x armv7hl aarch64
%global has_valgrind 1
%endif

Name:           gcr
Version:        3.14.0
Release:        1%{?dist}
Summary:        A library for bits of crypto UI and parsing

Group:          Development/Libraries
License:        LGPLv2+
URL:            http://live.gnome.org/CryptoGlue/
Source0:        http://download.gnome.org/sources/gcr/3.14/gcr-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  p11-kit-devel
BuildRequires:  gnupg
BuildRequires:  libgcrypt-devel
BuildRequires:  libtasn1-tools
BuildRequires:  libtasn1-devel
BuildRequires:  chrpath
BuildRequires:  vala-devel
BuildRequires:  vala-tools
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
%if 0%{?has_valgrind}
BuildRequires:  valgrind-devel
%endif

Conflicts: gnome-keyring < 3.3.0

%description
gcr is a library for displaying certificates, and crypto UI, accessing
key stores. It also provides a viewer for crypto files on the GNOME
desktop.

gck is a library for accessing PKCS#11 modules like smart cards.

%package devel
Summary: Development files for gcr
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The gcr-devel package includes the header files for the gcr library.


%prep
%setup -q

# Use system valgrind headers instead
%if 0%{?has_valgrind}
rm -rf build/valgrind/
%endif

%build
%configure --enable-introspection
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libmock-test-module.*
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gcr-viewer.desktop
%find_lang %{name}

chrpath --delete $RPM_BUILD_ROOT%{_libdir}/lib*.so.*
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/gcr-viewer
chrpath --delete $RPM_BUILD_ROOT%{_libexecdir}/gcr-prompter

%post
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :


%postun
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/update-mime-database -n %{_datadir}/mime &> /dev/null || :


%files -f %{name}.lang
%doc COPYING
%{_bindir}/gcr-viewer
%{_datadir}/applications/gcr-viewer.desktop
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/org.gnome.crypto.pgp.convert
%{_datadir}/GConf/gsettings/org.gnome.crypto.pgp_keyservers.convert
%{_datadir}/glib-2.0/schemas/org.gnome.crypto.pgp.gschema.xml
%{_libdir}/girepository-1.0
%{_libdir}/libgck-1.so.*
%{_libdir}/libgcr-3.so.*
%{_libdir}/libgcr-base-3.so.*
%{_libdir}/libgcr-ui-3.so.*
%{_datadir}/gcr-3
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/gcr-crypto-types.xml
%{_libexecdir}/gcr-prompter
%{_datadir}/dbus-1/services/org.gnome.keyring.PrivatePrompter.service
%{_datadir}/dbus-1/services/org.gnome.keyring.SystemPrompter.service
%{_datadir}/applications/gcr-prompter.desktop

%files devel
%{_includedir}/gck-1
%{_includedir}/gcr-3
%{_libdir}/libgck-1.so
%{_libdir}/libgcr-3.so
%{_libdir}/libgcr-base-3.so
%{_libdir}/libgcr-ui-3.so
%{_libdir}/pkgconfig/gck-1.pc
%{_libdir}/pkgconfig/gcr-3.pc
%{_libdir}/pkgconfig/gcr-base-3.pc
%{_libdir}/pkgconfig/gcr-ui-3.pc
%{_datadir}/gir-1.0
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gck
%{_datadir}/gtk-doc/html/gcr-3
%{_datadir}/vala/


%changelog
* Tue May 19 2015 David King <dking@redhat.com> - 3.14.0-1
- Update to 3.14.0 (#1222974)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.2-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.2-3
- Mass rebuild 2013-12-27

* Fri May 10 2013 Adam Williamson <awilliam@redhat.com> - 3.8.2-2
- update scriptlets to match current guidelines

* Sun May 05 2013 Stef Walter <stefw@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Tue Apr 16 2013 Richard Hughes <rhughes@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Mon Mar 18 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Mon Jan 14 2013 Tomas Bzatek <tbzatek@redhat.com> - 3.7.2-2
- Fix crash on parsing some certificates (#894157)

* Wed Jan 09 2013 Richard Hughes <hughsient@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Tue Aug 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.5-1
- Update to 3.5.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Mon Jun 25 2012 Richard Hughes <hughsient@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-2
- Silence glib-compile-schemas output

* Mon Apr 16 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Mon Mar 26 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.92-2
- Enable introspection, needed for gnome-shell now

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Fri Mar 09 2012 Rex Dieter <rdieter@fedoraproject.org> 3.3.90-2
- suppress scriptlet output

* Mon Mar  5 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90-1
- Update to 3.3.90

* Mon Feb 13 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan  3 2012 Tomas Bzatek <tbzatek@redhat.com> 3.3.3.1-4
- Add a Conflicts directive for older gnome-keyring packages (#771299)

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> 3.3.3.1-3
- Own some directories

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> 3.3.3.1-2
- Delete rpaths

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> 3.3.3.1-1
- Update to 3.3.3.1

* Fri Dec 15 2011 Matthias Clasen <mclasen@redhat.com> 3.3.2.1-1
- Update to 3.3.2.1

* Thu Nov 10 2011 Matthias Clasen <mclasen@redhat.com> 3.3.1-1
- Initial packaging

