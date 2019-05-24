#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx/BitBucket integration module for Python 2
Summary(pl.UTF-8):	Moduł integrujący Sphinx/BitBucket dla Pythona 2
Name:		python-sphinxcontrib-bitbucket
Version:	1.0
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-bitbucket/sphinxcontrib-bitbucket-%{version}.tar.gz
# Source0-md5:	129147d406087e44769ae7320a2d839b
Patch0:		%{name}-py3.patch
URL:		http://www.doughellmann.com/projects/sphinxcontrib-bitbucket/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 2
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds custom roles for linking to resources on BitBucket
projects.

%description -l pl.UTF-8
Ten moduł dodaje własne role, pozwalające na dowiązywanie do zasobów
projektów na serwisie BitBucket.

%package -n python3-sphinxcontrib-bitbucket
Summary:	Sphinx/BitBucket integration module for Python 3
Summary(pl.UTF-8):	Moduł integrujący Sphinx/BitBucket dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 3

%description -n python3-sphinxcontrib-bitbucket
This module adds custom roles for linking to resources on BitBucket
projects.

%description -n python3-sphinxcontrib-bitbucket -l pl.UTF-8
Ten moduł dodaje własne role, pozwalające na dowiązywanie do zasobów
projektów na serwisie BitBucket.

%prep
%setup -q -n sphinxcontrib-bitbucket-%{version}
%patch -p1

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README
# XXX: shared dir
%dir %{py_sitescriptdir}/sphinxcontrib
%{py_sitescriptdir}/sphinxcontrib/bitbucket.py[co]
%{py_sitescriptdir}/sphinxcontrib_bitbucket-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_bitbucket-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-bitbucket
%defattr(644,root,root,755)
%doc LICENSE README
# XXX: shared dirs
%dir %{py3_sitescriptdir}/sphinxcontrib
%dir %{py3_sitescriptdir}/sphinxcontrib/__pycache__
%{py3_sitescriptdir}/sphinxcontrib/bitbucket.py
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/bitbucket.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib_bitbucket-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_bitbucket-%{version}-py*-nspkg.pth
%endif
