%global packname  caTools
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.12
Release:          1
Summary:          Tools: moving window statistics, GIF, Base64, ROC AUC, etc
Group:            Sciences/Mathematics
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-bitops 
Requires:         R-MASS R-rpart 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-bitops
BuildRequires:    R-MASS R-rpart 

%description
Contains several basic utility functions including: moving (rolling,
running) window statistic functions, read/write for GIF and ENVI binary
files, fast calculation of AUC, LogitBoost classifier, base64
encoder/decoder, round-off error free sum and cumsum, etc.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
