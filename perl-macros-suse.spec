#
# spec file for package perl-macros
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
# 
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           perl-macros-suse
Summary:        Perl macros for rpm build
Version:        1.0
Release:        2
License:        GPL
Group:          Development/Libraries/Perl
Source0:        macros.perl
Source1:        README
Patch0:         %{name}_rhel.patch
BuildArch:      noarch
Provides:       perl_gen_filelist
%if 0%{?suse_version}
Provides:       perl-macros
Conflicts:      perl-macros
Requires:       perl
%endif
%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?fedora_version}
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(Test::More)
%if 0%{?fedora}
Requires:       perl-devel
%endif
Requires:       perl-macros
%endif


%description
This package provides perl rpm macros.
You need it for building perl modules

  Authors:
                Christian Wittmer <chris@computersalat.de>


%prep
%{__cp} %{S:0} .
%{__cp} %{S:1} .
%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?fedora_version}
%patch -P0 -p0
%endif

%build

%if 0%{?suse_version}
%if %suse_version < 1140
%post
# most evil hack ever - rpm does not sort the macros, so we need to rename the old one
cp %{_sysconfdir}/rpm/macros.suse-perl %{_sysconfdir}/rpm/macros.perl
%endif
%endif

%install
# make sure it overwrites macros.perl if sorted alphabetically
%{__install} -D -m644 macros.perl ${RPM_BUILD_ROOT}%{_sysconfdir}/rpm/macros.suse-perl

%files
%defattr(-,root,root)
%doc README
%{_sysconfdir}/rpm/macros.*

%changelog
