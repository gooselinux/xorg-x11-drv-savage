%define tarball xf86-video-savage
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 savage video driver
Name:      xorg-x11-drv-savage
Version:   2.3.1
Release:   1.1%{?dist}
URL:       http://www.x.org
License: MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:   savage.xinf

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-devel >= 1.4.99.1
BuildRequires: mesa-libGL-devel >= 6.4-4
BuildRequires: libdrm-devel >= 2.0-1

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.4.99.1

%description 
X.Org X11 savage video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static --enable-dri
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/savage_drv.so
%{_datadir}/hwdata/videoaliases/savage.xinf
%{_mandir}/man4/savage.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.3.1-1.1
- Rebuilt for RHEL 6

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 2.3.1-1
- savage 2.3.1

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 2.3.0-1.1
- ABI bump

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 2.3.0-1
- savage 2.3.0

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 2.2.0-2
- new server API rebuild

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 2.2.0-1
- Latest upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.3-101.20071210
- Autorebuild for GCC 4.3

* Wed Jan 09 2008 Adam Jackson <ajax@redhat.com> 2.1.3-100.20071210
- Rebuild for new server ABI.
- savage-2.1.3-alloca.patch: Fix {DE,}ALLOCATE_LOCAL usage.

* Mon Dec 10 2007 Adam Jackson <ajax@redhat.com> 2.1.3-99.20071210
- Today's git snapshot, for pciaccess goodness.

* Mon Aug 17 2007 Dave Airlie <airlied@redhat.com>  2.1.3-1
* Update to 2.1.3

* Mon Jul 09 2007 Adam Jackson <ajax@redhat.com> 2.1.2-5
- savage-2.1.2-panel-range-hack.patch: If we find a panel but no EDID,
  stretch the sync ranges out to fit the panel size. (#243589)

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 2.1.2-4
- Update Requires and BuildRequires.  Add Requires: hwdata.

* Mon Feb 26 2007 Adam Jackson <ajax@redhat.com> 2.1.2-3
- Delete a call to a symbol that's never existed.  Wacky.
- Disown the module directory

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 2.1.2-2
- ExclusiveArch -> ExcludeArch
- Enable DRI on all arches

* Mon Jan 29 2007 Adam Jackson <ajax@redhat.com> 2.1.2-1
- Update to 2.1.2

* Mon Jul 24 2006 Mike A. Harris <mharris@redhat.com> 2.1.1-5.fc6
- Added savage-disable-dri-bug196011.patch to disable DRI by default on various
  Savage chipsets reported in bug (#196011) and (fdo#6357)
- Added {?dist} tag to Release field.

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> 2.1.1-4
- rebuild

* Fri May 26 2006 Mike A. Harris <mharris@redhat.com> 2.1.1-3
- Added "BuildRequires: libdrm-devel >= 2.0-1" for DRI enabled builds (#192349)

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 2.1.1-2
- Rebuild for 7.1 ABI fix.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 2.1.1-1
- Update to 2.1.1 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.0.2.3-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.0.2.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 2.0.2.3-1
- Updated xorg-x11-drv-savage to version 2.0.2.3 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 2.0.2.2-1
- Updated xorg-x11-drv-savage to version 2.0.2.2 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 2.0.2-1
- Updated xorg-x11-drv-savage to version 2.0.2 from X11R7 RC2
- Added "BuildRequires: mesa-libGL-devel >= 6.4-4" for DRI-enabled builds.

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 2.0.1.1-1
- Updated xorg-x11-drv-savage to version 2.0.1.1 from X11R7 RC1
- Fix *.la file removal.

* Tue Oct 4 2005 Mike A. Harris <mharris@redhat.com> 2.0.0-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to x86, x86_64, ppc

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 2.0.0-0
- Initial spec file for savage video driver generated automatically
  by my xorg-driverspecgen script.
