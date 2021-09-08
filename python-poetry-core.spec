%global debug_package %{nil}

Name: python-poetry-core
Epoch: 100
Version: 1.0.5
Release: 1%{?dist}
BuildArch: noarch
Summary: Poetry PEP 517 Build Backend
License: MIT
URL: https://github.com/python-poetry/poetry-core/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A PEP 517 build backend implementation developed for Poetry. This
project is intended to be a light weight, fully compliant,
self-contained package allowing PEP 517 compatible build frontends to
build Poetry managed projects.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-poetry-core
Summary: Poetry PEP 517 Build Backend
Requires: python3
Requires: python3-importlib-metadata >= 1.7.0
Provides: python3-poetry-core = %{epoch}:%{version}-%{release}
Provides: python3dist(poetry-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-poetry-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(poetry-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-poetry-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(poetry-core) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-poetry-core
A PEP 517 build backend implementation developed for Poetry. This
project is intended to be a light weight, fully compliant,
self-contained package allowing PEP 517 compatible build frontends to
build Poetry managed projects.

%files -n python%{python3_version_nodots}-poetry-core
%license LICENSE
%dir %{python3_sitelib}/poetry
%{python3_sitelib}/poetry/*
%{python3_sitelib}/poetry_core*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-poetry-core
Summary: Poetry PEP 517 Build Backend
Requires: python3
Requires: python3-importlib-metadata >= 1.7.0
Provides: python3-poetry-core = %{epoch}:%{version}-%{release}
Provides: python3dist(poetry-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-poetry-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(poetry-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-poetry-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(poetry-core) = %{epoch}:%{version}-%{release}

%description -n python3-poetry-core
A PEP 517 build backend implementation developed for Poetry. This
project is intended to be a light weight, fully compliant,
self-contained package allowing PEP 517 compatible build frontends to
build Poetry managed projects.

%files -n python3-poetry-core
%license LICENSE
%dir %{python3_sitelib}/poetry
%{python3_sitelib}/poetry/*
%{python3_sitelib}/poetry_core*
%endif

%changelog
