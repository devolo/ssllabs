# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Query used API version with ssllabs.api.API_VERSION
- Low level methods now can reuse an existing AsyncClient instance

## [v0.2.0] - 2021/01/28

### Added

- High level methods now respect cool off and maximum assessment rate limits

## [v0.1.1] - 2021/01/27

### Fixed

- Fixed pip installation

## [v0.1.0] - 2021/01/27

### Added

- High level usage methods
- Low level info API
- Low level analyze API
- Low level getEndpointData API
- Low level getStatusCodes API
- Low level getRootCertsRaw API
