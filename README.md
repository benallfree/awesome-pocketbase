# Awesome PocketBase [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![GitHub forks](https://img.shields.io/github/stars/benallfree/awesome-pocketbase?style=flat) ![GitHub forks](https://img.shields.io/github/forks/benallfree/awesome-pocketbase?style=flat) ![GitHub forks](https://img.shields.io/github/contributors/benallfree/awesome-pocketbase?style=flat)

> Curated list of awesome [PocketBase](https://pocketbase.io) resources.

PocketBase is an open source backend consisting of embedded database (SQLite) with realtime subscriptions, built-in auth management, convenient dashboard UI and simple REST-ish API.

## Contents

- [Official Packages](#official-packages)
- [Major Community Projects](#major-community-projects)
- [JSVM Plugins](#jsvm-plugins)
- [Go Plugins](#go-plugins)
- [React](#react)
- [Svelte](#svelte)
- [Vue](#vue)
- [Solid](#solid)
- [Dart/Flutter](#dartflutter)
- [C#](#c)
- [D](#d)
- [Node.js](#nodejs)
- [Unofficial PocketBase Clients (SDKs)](#unofficial-pocketbase-clients-sdks)
- [Self Hosting](#self-hosting)
- [TypeScript tools](#typescript-tools)
- [SQLite tools](#sqlite-tools)
- [Other tools](#other-tools)
- [Showcases](#showcases)
- [PocketPorts Packages](#pocketports-packages)

## Official Packages

- [Golang Server](https://github.com/pocketbase/pocketbase/releases/) - The main PocketBase server. ![GitHub Repo stars](https://img.shields.io/github/stars/pocketbase/pocketbase)

- [JavaScript SDK](https://github.com/pocketbase/js-sdk) - Browser and Node.js for interacting with the PocketBase API. ![GitHub Repo stars](https://img.shields.io/github/stars/pocketbase/js-sdk)
- [Dart SDK](https://github.com/pocketbase/dart-sdk) - Multi-platform SDK for interacting with the PocketBase Web API. ![GitHub Repo stars](https://img.shields.io/github/stars/pocketbase/dart-sdk)

## Top PocketBase-specific Projects (>100 stars)

- [pockethost.io](https://pockethost.io) - Free and pro PocketBase hosting. ![GitHub Repo stars](https://img.shields.io/github/stars/pockethost/pockethost)
- [PocketBase Typegen](https://github.com/patmood/pocketbase-typegen) - Generate TypeScript types from the SQLite db file. ![GitHub Repo stars](https://img.shields.io/github/stars/patmood/pocketbase-typegen)
- [PocketBase Docker](https://github.com/muchobien/pocketbase-docker) - Docker setup supporting multiple architectures and automatically updated with PocketBase releases. ![GitHub Repo stars](https://img.shields.io/github/stars/muchobien/pocketbase-docker)
- [PocketBase+Stripe](https://github.com/mrwyndham/pocketbase-stripe) - Go extended PocketBase for Stripe subscription integration. ![GitHub Repo stars](https://img.shields.io/github/stars/mrwyndham/pocketbase-stripe)
- [SvelteKit Starter](https://github.com/spinspire/pocketbase-sveltekit-starter) - A starter-kit showing how to use customized PocketBase as a backend to SvelteKit frontend. ![GitHub Repo stars](https://img.shields.io/github/stars/spinspire/pocketbase-sveltekit-starter)
- [SvelteKit Auth](https://github.com/danawoodman/sveltekit-auth-example) - This project is designed as a sample implementation reference for getting authentication setup using SvelteKit. ![GitHub Repo stars](https://img.shields.io/github/stars/danawoodman/sveltekit-auth-example)
- [SvelteKit PocketBase Auth](https://github.com/jianyuan/pocketbase-sveltekit-auth) - Demo login and registration pages with examples. [video](https://youtu.be/AxPB3e-3yEM). ![GitHub Repo stars](https://img.shields.io/github/stars/jianyuan/pocketbase-sveltekit-auth)


## Major Community Projects

- [pocketpages.dev](https://pocketpages.dev) - Server-side JS pages and hosting for PocketBase. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/pocketpages)
- [pockethost.io](https://pockethost.io) - Free and pro PocketBase hosting. ![GitHub Repo stars](https://img.shields.io/github/stars/pockethost/pockethost)
- [pocodex.dev](https://pocodex.dev) - The unofficial PocketBase plugin repository and code exchange. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/pocodex)
- PocketPorts - NPM/Node.js packages ported to PocketBase JSVM. Official listing is hosted here in awesome-pocketbase.

## JSVM Plugins

* [pocketbase-otp](https://github.com/benallfree/pocketbase-otp) - One-Time Passwords for <=v0.22.* ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/pocketbase-otp)
* [pocketpages](https://github.com/benallfree/pocketpages) - Server-side EJS pages for PocketBase. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/pocketpages)
* [pocketbase-presigned-urls](https://github.com/benallfree/pocketbase-presigned-urls) - Serve file uploads from presigned S3 URLs. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/pocketbase-presigned-urls)

## Go Plugins

- [Telegram auth](https://github.com/iamelevich/pocketbase-plugin-telegram-auth) - Add Telegram auth (Widget button and WebApp). ![GitHub Repo stars](https://img.shields.io/github/stars/iamelevich/pocketbase-plugin-telegram-auth)
- [Ngrok](https://github.com/iamelevich/pocketbase-plugin-ngrok) - Expose local PocketBase to the internet with ngrok. ![GitHub Repo stars](https://img.shields.io/github/stars/iamelevich/pocketbase-plugin-ngrok)
- [Proxy](https://github.com/iamelevich/pocketbase-plugin-proxy) - Proxy requests to another other host. Can be useful when you want to use separate server as frontend (like Next.js), but serve everything with same port. ![GitHub Repo stars](https://img.shields.io/github/stars/iamelevich/pocketbase-plugin-proxy)
- [Webhooks](https://gist.github.com/cugu/9e74f75dcad3df74370c71ff3c02085a) - Add webhook support in the admin UI to send `create`, `update` and `delete` events on selected collections via POST request to other systems.

## React

- [PocketBase React](https://github.com/tobicrain/pocketbase-react) - Unofficial React SDK (React, React Native, Expo) for interacting with the PocketBase JavaScript SDK. ![GitHub Repo stars](https://img.shields.io/github/stars/tobicrain/pocketbase-react)
- [PocketBase Next.js App Template](https://github.com/tsensei/nextjs-pocketbase-starter-template) - PocketBase Next.js Template with server & browser client using cookies. ![GitHub Repo stars](https://img.shields.io/github/stars/tsensei/nextjs-pocketbase-starter-template)

## Svelte

- [svelte-query-pocketbase](https://github.com/goknsh/svelte-query-pocketbase) - TanStack Query wrappers around PocketBase for Svelte and SvelteKit that updates the query cache in realtime. ![GitHub Repo stars](https://img.shields.io/github/stars/goknsh/svelte-query-pocketbase)
- [SvelteKit Starter](https://github.com/spinspire/pocketbase-sveltekit-starter) - A starter-kit showing how to use customized PocketBase as a backend to SvelteKit frontend. ![GitHub Repo stars](https://img.shields.io/github/stars/spinspire/pocketbase-sveltekit-starter)
- [SvelteKit Auth](https://github.com/danawoodman/sveltekit-auth-example) - This project is designed as a sample implementation reference for getting authentication setup using SvelteKit. ![GitHub Repo stars](https://img.shields.io/github/stars/danawoodman/sveltekit-auth-example)
- [SvelteKit PocketBase Auth](https://github.com/jianyuan/pocketbase-sveltekit-auth) - Demo login and registration pages with examples. [video](https://youtu.be/AxPB3e-3yEM). ![GitHub Repo stars](https://img.shields.io/github/stars/jianyuan/pocketbase-sveltekit-auth)
- [pocketbase-sveltekit-static](https://github.com/Egor-S/pocketbase-sveltekit-static) - A minimalist template with configured authorization featuring a single Docker image (from 55 MB) for deploying. ![GitHub Repo stars](https://img.shields.io/github/stars/Egor-S/pocketbase-sveltekit-static)

## Vue

- [Vue 3 + Vite starter kit](https://github.com/StefanVDWeide/pocketbase-vue) - A starter kit for Vue 3 + Vite + PocketBase. ![GitHub Repo stars](https://img.shields.io/github/stars/StefanVDWeide/pocketbase-vue)
- [Tutorial](https://studioterabyte.nl/en/blog/pocketbase-vue-3) - Vue 3 tutorial.
- [Quasar starter kit](https://github.com/aaronblondeau/pocketbase_quasar_starter) - Pocketbase with Quasar. ![GitHub Repo stars](https://img.shields.io/github/stars/aaronblondeau/pocketbase_quasar_starter)
- [PocketNuxt](https://github.com/j-wil/pocket-nuxt) - A Nuxt3 PocketBase starter that builds into a single binary. ![GitHub Repo stars](https://img.shields.io/github/stars/j-wil/pocket-nuxt)

## Solid

- [Solid-pocketbase-hooks](https://github.com/kirill-dev-pro/solid-pocketbase-hooks) - Pocketbase hooks for Solid.js ![GitHub Repo stars](https://img.shields.io/github/stars/kirill-dev-pro/solid-pocketbase-hooks)

## Dart/Flutter

- [PocketBase Drift](https://github.com/rodydavis/pocketbase_drift) - A PocketBase client cached with Drift. ![GitHub Repo stars](https://img.shields.io/github/stars/rodydavis/pocketbase_drift)
- [Dart Generator](https://github.com/rodydavis/pocketbase_dart_generator) - Generate type safe client SDKs for use in local SQLite, JSON or GraphQL resolvers. ![GitHub Repo stars](https://img.shields.io/github/stars/rodydavis/pocketbase_dart_generator)
- [PocketBase Server Flutter](https://github.com/rohitsangwan01/pocketbase_server_flutter) - A Flutter plugin to run PocketBase server directly from Android/iOS. ![GitHub Repo stars](https://img.shields.io/github/stars/rohitsangwan01/pocketbase_server_flutter)

## C#

- [ORM and code generator](https://github.com/iluvadev/PocketBaseClient-csharp) - An ORM to manage your PocketBase Application. ![GitHub Repo stars](https://img.shields.io/github/stars/iluvadev/PocketBaseClient-csharp)

## D

- [libpb](https://github.com/Hax-io/libpb) - PocketBase client wrapper for D with automatic serialization and deserialization to and from JSON. ![GitHub Repo stars](https://img.shields.io/github/stars/Hax-io/libpb)

## Node.js

- [gobot](https://github.com/benallfree/gobot) - PocketBase as an npm package. CLI and API. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/gobot)

## Unofficial PocketBase Clients (SDKs)

- [Go](https://github.com/pluja/pocketbase) - PocketBase Client in Golang. ![GitHub Repo stars](https://img.shields.io/github/stars/pluja/pocketbase)
- [Kotlin](https://github.com/agrevster/pocketbase-kotlin) - PocketBase Client in Kotlin. ![GitHub Repo stars](https://img.shields.io/github/stars/agrevster/pocketbase-kotlin)
- [Kotlin (Multiplatform)](https://github.com/IdanAizikNissim/pocketbase-kt) - PocketBase Client in Kotlin. ![GitHub Repo stars](https://img.shields.io/github/stars/IdanAizikNissim/pocketbase-kt)
- [Python (Sync)](https://github.com/vaphes/pocketbase) - PocketBase Client in Python. ![GitHub Repo stars](https://img.shields.io/github/stars/vaphes/pocketbase)
- [Python (Async)](https://github.com/thijsmie/pocketbase) - PocketBase Client in Python. ![GitHub Repo stars](https://img.shields.io/github/stars/thijsmie/pocketbase)
- [C#](https://github.com/PRCV1/pocketbase-csharp-sdk) - PocketBase Client in C#. ![GitHub Repo stars](https://img.shields.io/github/stars/PRCV1/pocketbase-csharp-sdk)
- [Rust](https://github.com/sreedevk/pocketbase-sdk-rust) - PocketBase Client in Rust. ![GitHub Repo stars](https://img.shields.io/github/stars/sreedevk/pocketbase-sdk-rust)
- [PHP](https://github.com/mkay-development/pocketbase-php-sdk) - PocketBase Client in PHP. ![GitHub Repo stars](https://img.shields.io/github/stars/mkay-development/pocketbase-php-sdk)

## Self Hosting

- [PocketBase Docker](https://github.com/muchobien/pocketbase-docker) - Docker setup supporting multiple architectures and automatically updated with PocketBase releases. ![GitHub Repo stars](https://img.shields.io/github/stars/muchobien/pocketbase-docker)
- [DigitalOcean](https://github.com/pocketbase/pocketbase/discussions/512) - Guide to deploy in a Droplet.
- [Fly.io](https://github.com/pocketbase/pocketbase/discussions/537) - Guide to deploy for free in Fly.io.
- [LocalXpose](https://localxpose.io/docs/tutorials/expose-pocketbase-backend) - Allow public access to a localhost instance.
- [PocketBase Docker](https://github.com/kdpuvvadi/pocketbase) - Docker images supporting multiple architectures and updated with latest PocketBase releases. ![GitHub Repo stars](https://img.shields.io/github/stars/kdpuvvadi/pocketbase)
- [PocketBase on Dokku](https://github.com/blockshiftnetwork/dokku-pocketbase) - Deploy PocketBase instances on Dokku effortlessly. ![GitHub Repo stars](https://img.shields.io/github/stars/blockshiftnetwork/dokku-pocketbase)

## TypeScript tools

- [pocketbase-jsvm](https://github.com/benallfree/pocketbase-jsvm) - JSVM typings. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/pocketbase-jsvm)
- [pb_hooks starter kit](https://github.com/benallfree/ts-pb-hooks-starter) - Build PocketBase JavaScript hooks using TypeScript. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/ts-pb-hooks-starter)
- [PocketBase Typegen](https://github.com/patmood/pocketbase-typegen) - Generate TypeScript types from the SQLite db file. ![GitHub Repo stars](https://img.shields.io/github/stars/patmood/pocketbase-typegen)
- [typed-pocketbase](https://github.com/david-plugge/typed-pocketbase) - Generate types from your PocketBase instance and enjoy fully type-safe queries. ![GitHub Repo stars](https://img.shields.io/github/stars/david-plugge/typed-pocketbase)
- [pocketbase-ts](https://github.com/satohshi/pocketbase-ts) — SDK wrapper with more readable `options` syntax and full type-safety. ![GitHub Repo stars](https://img.shields.io/github/stars/satohshi/pocketbase-ts)

## SQLite tools

- [Marmot](https://github.com/maxpert/marmot) - A distributed SQLite replicator [with PocketBase tutorial](https://www.youtube.com/watch?v=Zapupe_FREc). ![GitHub Repo stars](https://img.shields.io/github/stars/maxpert/marmot)
- [Litestream](https://litestream.io/) - Streaming SQLite replication. ![GitHub Repo stars](https://img.shields.io/github/stars/benbjohnson/litestream)
- [PocketBase+Litestream example](https://github.com/TylerSustare/pocketbase-framework-litestream) - Template showing Litestream running with PocketBase. ![GitHub Repo stars](https://img.shields.io/github/stars/TylerSustare/pocketbase-framework-litestream)
- [PocketBase with Litestream](https://github.com/bscott/pocketbase-litestream/) - Docker example of PocketBase saving/restoring from Litestream. ![GitHub Repo stars](https://img.shields.io/github/stars/bscott/pocketbase-litestream)

## Other tools

- [PocketBaseUML](https://pocketbase-uml.github.io/) - A free, open-source web application that generates UML diagrams based on PocketBase databases. ![GitHub Repo stars](https://img.shields.io/github/stars/bscott/pocketbase-litestream)
- [PocketBaseMobile](https://github.com/rohitsangwan01/pocketbase_mobile) - Android and iOS frameworks for running PocketBase from mobile. ![GitHub Repo stars](https://img.shields.io/github/stars/rohitsangwan01/pocketbase_mobile)
- [PocketBase+Stripe](https://github.com/mrwyndham/pocketbase-stripe) - Go extended PocketBase for Stripe subscription integration. ![GitHub Repo stars](https://img.shields.io/github/stars/mrwyndham/pocketbase-stripe)
- [pbf](https://github.com/nedpals/pbf) - Library for serializing and deserializing PocketBase filter syntax. ![GitHub Repo stars](https://img.shields.io/github/stars/nedpals/pbf)
- [PocketBase Templates](https://github.com/Pocket-Space/pocketbase-templates) - A open-source collection of PocketBase schemas to quickly get started. ![GitHub Repo stars](https://img.shields.io/github/stars/Pocket-Space/pocketbase-templates)
- [pocketbase-queue](https://github.com/joseferben/pocketbase-queue) - A type-safe queue for background tasks using PocketBase. ![GitHub Repo stars](https://img.shields.io/github/stars/joseferben/pocketbase-queue)
- [PocketBase GPT](https://chat.openai.com/g/g-Owo2FBp4K-pocketbase-gpt) - A GPT that has all of PocketBase's documentation uploaded to it, to give more accurate and up-to-date answers.

## Showcases

- [Vimsnake](https://github.com/patmood/vim_snake) - A realtime WASM game where Vim commands are used as controller inputs. ![GitHub Repo stars](https://img.shields.io/github/stars/patmood/vim_snake)
- [ToDo](https://github.com/rajesh6161/pocketbaseTodo) - React-based To-Do demo app. ![GitHub Repo stars](https://img.shields.io/github/stars/rajesh6161/pocketbaseTodo)
- [Realtime Blog](https://github.com/rajesh6161/pbRealtimeBlog) - A React-based realtime blog demo. ![GitHub Repo stars](https://img.shields.io/github/stars/rajesh6161/pbRealtimeBlog)
- [oAuth](https://github.com/rajesh6161/pocketbase-oauth-demo) - A React-based oAuth demo. ![GitHub Repo stars](https://img.shields.io/github/stars/rajesh6161/pocketbase-oauth-demo)
- [Flutter Chat App](https://github.com/rohitsangwan01/flutter_pocketbase_chat) - A chat app using PocketBase in Flutter. ![GitHub Repo stars](https://img.shields.io/github/stars/rohitsangwan01/flutter_pocketbase_chat)
- [JustJot](https://justjot.app) - A keyboard-first note-taking full-featured Progressive Web App. [frontend repo](https://github.com/JunoNgx/justjot-frontend) / [backend repo](https://github.com/JunoNgx/justjot-backend) ![GitHub Repo stars](https://img.shields.io/github/stars/JunoNgx/justjot-backend)
- [Cookie auth demo](https://github.com/davidbarton/pocketbase-cookie-auth-demo) - A demo of cookie based authentication flow for PocketBase. ![GitHub Repo stars](https://img.shields.io/github/stars/davidbarton/pocketbase-cookie-auth-demo)

## PocketPorts Packages

Ports of NPM/Node.js packages to the PocketBase JSVM.

| OG Package                                     | Ported Package                                                   | Description                                                    |                                                                                      |
| ---------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [Node.js](https://nodejs.org/docs/latest/api/) | [pocketbase-node](https://github.com/benallfree/pocketbase-node) | Node.js core packages (`fs`, `process`, etc)                   | ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/pocketbase-node) |
| [ejs](https://github.com/mde/ejs)              | [pocketbase-ejs](https://github.com/benallfree/pocketbase-ejs)   | Embedded JavaScript templates - [http://ejs.co](http://ejs.co) | ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/pocketbase-ejs)  |
| [marked](https://github.com/markedjs/marked)   | ✅ works without changes                                         | A markdown parser and compiler. Built for speed.               | ![GitHub Repo stars](https://img.shields.io/github/stars/markedjs/marked)            |

