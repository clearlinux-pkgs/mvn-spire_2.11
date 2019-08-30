#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-spire_2.11
Version  : 0.13.0
Release  : 3
URL      : https://github.com/typelevel/spire/archive/v0.13.0.tar.gz
Source0  : https://github.com/typelevel/spire/archive/v0.13.0.tar.gz
Source1  : https://repo1.maven.org/maven2/org/spire-math/spire-macros_2.11/0.13.0/spire-macros_2.11-0.13.0.jar
Source2  : https://repo1.maven.org/maven2/org/spire-math/spire-macros_2.11/0.13.0/spire-macros_2.11-0.13.0.pom
Source3  : https://repo1.maven.org/maven2/org/spire-math/spire_2.11/0.13.0/spire_2.11-0.13.0.jar
Source4  : https://repo1.maven.org/maven2/org/spire-math/spire_2.11/0.13.0/spire_2.11-0.13.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-spire_2.11-data = %{version}-%{release}

%description
[![Build Status](https://api.travis-ci.org/non/spire.png)](https://travis-ci.org/non/spire/)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/non/spire?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![codecov.io](http://codecov.io/github/non/spire/coverage.svg?branch=master)](http://codecov.io/github/non/spire?branch=master)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/org.spire-math/spire_2.11/badge.svg)](https://maven-badges.herokuapp.com/maven-central/org.spire-math/spire_2.11)

%package data
Summary: data components for the mvn-spire_2.11 package.
Group: Data

%description data
data components for the mvn-spire_2.11 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spire-math/spire-macros_2.11/0.13.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/spire-math/spire-macros_2.11/0.13.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spire-math/spire-macros_2.11/0.13.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/spire-math/spire-macros_2.11/0.13.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spire-math/spire_2.11/0.13.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/spire-math/spire_2.11/0.13.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spire-math/spire_2.11/0.13.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/spire-math/spire_2.11/0.13.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/spire-math/spire-macros_2.11/0.13.0/spire-macros_2.11-0.13.0.jar
/usr/share/java/.m2/repository/org/spire-math/spire-macros_2.11/0.13.0/spire-macros_2.11-0.13.0.pom
/usr/share/java/.m2/repository/org/spire-math/spire_2.11/0.13.0/spire_2.11-0.13.0.jar
/usr/share/java/.m2/repository/org/spire-math/spire_2.11/0.13.0/spire_2.11-0.13.0.pom
