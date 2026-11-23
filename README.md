# Awesome PocketBase [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![GitHub forks](https://img.shields.io/github/stars/benallfree/awesome-pocketbase?style=flat) ![GitHub forks](https://img.shields.io/github/forks/benallfree/awesome-pocketbase?style=flat) ![GitHub forks](https://img.shields.io/github/contributors/benallfree/awesome-pocketbase?style=flat)

> Curated list of awesome [PocketBase](https://pocketbase.io) resources.

PocketBase is an open source backend consisting of embedded database (SQLite) with realtime subscriptions, built-in auth management, convenient dashboard UI and simple REST-ish API.

## Contents

- [Official Packages](#official-packages)
- [Forks](#forks)
- [Top PocketBase-specific Projects (\>100 stars)](#top-pocketbase-specific-projects-100-stars)
- [Major Community Projects](#major-community-projects)
- [JSVM Plugins](#jsvm-plugins)
- [Go Plugins](#go-plugins)
- [React](#react)
- [Svelte](#svelte)
- [Dart/Flutter](#dartflutter)
- [C#](#c)
- [Unofficial PocketBase Clients (SDKs)](#unofficial-pocketbase-clients-sdks)
- [Self Hosting](#self-hosting)
- [TypeScript tools](#typescript-tools)
- [SQLite tools](#sqlite-tools)
- [Other tools](#other-tools)
- [Showcases](#showcases)
- [Unmaintained](#unmaintained)

## Official Packages

PocketBase moved its repositories from GitHub to [ganigeorgiev.com](https://ganigeorgiev.com/pocketbase); the GitHub repositories are archived. Star counts below are from the archived GitHub repositories.

- [Golang Server](https://ganigeorgiev.com/pocketbase/pocketbase/releases) - The main PocketBase server. ![GitHub Repo stars](https://img.shields.io/github/stars/pocketbase/pocketbase)

- [JavaScript SDK](https://ganigeorgiev.com/pocketbase/js-sdk) - Browser and Node.js for interacting with the PocketBase API. ![GitHub Repo stars](https://img.shields.io/github/stars/pocketbase/js-sdk)
- [Dart SDK](https://ganigeorgiev.com/pocketbase/dart-sdk) - Multi-platform SDK for interacting with the PocketBase Web API. ![GitHub Repo stars](https://img.shields.io/github/stars/pocketbase/dart-sdk)

## Forks

- [PostgreBase](https://github.com/zhenruyan/postgrebase) - A PocketBase fork with PostgreSQL and MySQL support alongside SQLite, a built-in MCP server and Redis or in-memory caching, keeping the PocketBase API. ![GitHub Repo stars](https://img.shields.io/github/stars/zhenruyan/postgrebase)
- [PocketOne](https://pocketone.dev) - An open, community-driven fork of PocketBase. Features live in Go extensions that connect only through versioned contracts, so anyone can contribute (PITR, bulk mail, WASM, an updated JSVM, and more) without touching core. Not affiliated with PocketBase. ![GitHub Repo stars](https://img.shields.io/github/stars/pocketonehq/pocketone)

## Top PocketBase-specific Projects (>100 stars)

- [pockethost.io](https://pockethost.io) - Pro PocketBase hosting. ![GitHub Repo stars](https://img.shields.io/github/stars/pockethost/pockethost)
- [PocketBase Typegen](https://github.com/patmood/pocketbase-typegen) - Generate TypeScript types from the SQLite db file. ![GitHub Repo stars](https://img.shields.io/github/stars/patmood/pocketbase-typegen)
- [PocketBase Docker](https://github.com/muchobien/pocketbase-docker) - Docker setup supporting multiple architectures and automatically updated with PocketBase releases. ![GitHub Repo stars](https://img.shields.io/github/stars/muchobien/pocketbase-docker)
- [Python SDK](https://github.com/vaphes/pocketbase) - PocketBase client in Python. ![GitHub Repo stars](https://img.shields.io/github/stars/vaphes/pocketbase)
- [SvelteKit Starter](https://github.com/spinspire/pocketbase-sveltekit-starter) - A starter-kit showing how to use customized PocketBase as a backend to SvelteKit frontend. ![GitHub Repo stars](https://img.shields.io/github/stars/spinspire/pocketbase-sveltekit-starter)
- [SvelteKit PocketBase Auth](https://github.com/jianyuan/pocketbase-sveltekit-auth) - Demo login and registration pages with examples. ![GitHub Repo stars](https://img.shields.io/github/stars/jianyuan/pocketbase-sveltekit-auth)
- [PocketBase+Stripe](https://github.com/mrwyndham/pocketbase-stripe) - Go extended PocketBase for Stripe subscription integration. ![GitHub Repo stars](https://img.shields.io/github/stars/mrwyndham/pocketbase-stripe)
- [PocketBaseUML](https://pocketbase-uml.github.io/) - Generate UML diagrams from PocketBase databases. ![GitHub Repo stars](https://img.shields.io/github/stars/pocketbase-uml/pocketbase-uml.github.io)
- [pocketbase-mcp](https://github.com/mrwyndham/pocketbase-mcp) - MCP server for building PocketBase apps with AI assistants. ![GitHub Repo stars](https://img.shields.io/github/stars/mrwyndham/pocketbase-mcp)
- [pb-ext](https://github.com/magooney-loon/pb-ext) - Enhanced PocketBase server with monitoring, logging & API docs. ![GitHub Repo stars](https://img.shields.io/github/stars/magooney-loon/pb-ext)
- [refine-pocketbase](https://github.com/kruschid/refine-pocketbase) - Data, auth and live providers for building refine apps on PocketBase. ![GitHub Repo stars](https://img.shields.io/github/stars/kruschid/refine-pocketbase)
- [PocketBlocks](https://github.com/pedrozadotdev/pocketblocks) - Openblocks low-code app builder integrated with PocketBase. ![GitHub Repo stars](https://img.shields.io/github/stars/pedrozadotdev/pocketblocks)

## Major Community Projects

- [PocketPages](https://pocketone.dev/docs/extensions/pages) - Server-side JS pages for PocketBase, built into PocketOne.
- [PocketCon 2027](https://pocketcon.dev) - A free online PocketBase conference on Saturday, February 6, 2027.

## JSVM Plugins

- [pocketbase-presigned-urls](https://github.com/benallfree/pocketbase-presigned-urls) - Serve file uploads from presigned S3 URLs. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/pocketbase-presigned-urls)

## Go Plugins

- [pocketbase-ha](https://github.com/litesql/pocketbase-ha) - Highly available leader or leaderless PocketBase cluster built on the go-ha database/sql driver. ![GitHub Repo stars](https://img.shields.io/github/stars/litesql/pocketbase-ha)
- [Telegram auth](https://github.com/iamelevich/pocketbase-plugin-telegram-auth) - Add Telegram auth (Widget button and WebApp). ![GitHub Repo stars](https://img.shields.io/github/stars/iamelevich/pocketbase-plugin-telegram-auth)
- [pocketbase-gogen](https://github.com/Snonky/pocketbase-gogen) - Generate data model structs from a PocketBase schema. ![GitHub Repo stars](https://img.shields.io/github/stars/Snonky/pocketbase-gogen)
- [TypeScript Generator](https://github.com/Vogeslu/pocketbase-ts-generator) - Standalone tool or library that generates TypeScript types, with auto-generation hook or command. ![GitHub Repo stars](https://img.shields.io/github/stars/Vogeslu/pocketbase-ts-generator)
- [Proxy](https://github.com/iamelevich/pocketbase-plugin-proxy) - Forward requests to another host. Can be useful when you want to use separate server as frontend (like Next.js), but serve everything with same port. ![GitHub Repo stars](https://img.shields.io/github/stars/iamelevich/pocketbase-plugin-proxy)
- [Ngrok](https://github.com/iamelevich/pocketbase-plugin-ngrok) - Expose local PocketBase to the internet with ngrok. ![GitHub Repo stars](https://img.shields.io/github/stars/iamelevich/pocketbase-plugin-ngrok)
- [Webhooks](https://gist.github.com/cugu/9e74f75dcad3df74370c71ff3c02085a) - Add webhook support in the admin UI to send `create`, `update` and `delete` events on selected collections via POST request to other systems.

## React

- [PocketBase React](https://github.com/tobicrain/pocketbase-react) - Unofficial React SDK (React, React Native, Expo) for interacting with the PocketBase JavaScript SDK. ![GitHub Repo stars](https://img.shields.io/github/stars/tobicrain/pocketbase-react)
- [pbtsdb](https://github.com/nathanstitt/pbtsdb) - A type-safe TanStack DB adapter to easily create LiveQueries with real-time subscriptions. ![GitHub Repo stars](https://img.shields.io/github/stars/nathanstitt/pbtsdb)
- [Next.js PocketBase Auth](https://github.com/jianyuan/pocketbase-nextjs-auth) - Sample Next.js 15 application with PocketBase integration, a typed client, server-side and client-side rendering techniques, and server actions. ![GitHub Repo stars](https://img.shields.io/github/stars/jianyuan/pocketbase-nextjs-auth)
- [next-pocketbase-auth](https://github.com/g12i/next-pocketbase-auth) - A lightweight authentication wrapper for Next.js applications, providing easy-to-use utilities for handling user session in both client and server components. ![GitHub Repo stars](https://img.shields.io/github/stars/g12i/next-pocketbase-auth)

## Svelte

- [pocketbase-sveltekit-static](https://github.com/Egor-S/pocketbase-sveltekit-static) - A minimalist template with configured authorization featuring a single Docker image (from 55 MB) for deploying. ![GitHub Repo stars](https://img.shields.io/github/stars/Egor-S/pocketbase-sveltekit-static)

## Dart/Flutter

- [PocketBase Server Flutter](https://github.com/rohitsangwan01/pocketbase_server_flutter) - A Flutter plugin to run PocketBase server directly from Android/iOS. ![GitHub Repo stars](https://img.shields.io/github/stars/rohitsangwan01/pocketbase_server_flutter)

## C#

- [PocketBaseSharp](https://github.com/PSCourtney/PocketBaseSharp) - C# SDK for PocketBase and demo Blazor WebAssembly webapp. ![GitHub Repo stars](https://img.shields.io/github/stars/PSCourtney/PocketBaseSharp)

## Unofficial PocketBase Clients (SDKs)

- [Go](https://github.com/pluja/pocketbase) - PocketBase Client in Golang. ![GitHub Repo stars](https://img.shields.io/github/stars/pluja/pocketbase)
- [Python (Async)](https://github.com/thijsmie/pocketbase) - PocketBase Client in Python. ![GitHub Repo stars](https://img.shields.io/github/stars/thijsmie/pocketbase)
- [Swift](https://github.com/briannadoubt/PocketBase) - PocketBase client for iOS, macOS, watchOS, tvOS and visionOS. ![GitHub Repo stars](https://img.shields.io/github/stars/briannadoubt/PocketBase)
- [Rust](https://github.com/sreedevk/pocketbase-sdk-rust) - PocketBase Client in Rust. ![GitHub Repo stars](https://img.shields.io/github/stars/sreedevk/pocketbase-sdk-rust)
- [Kotlin](https://github.com/agrevster/pocketbase-kotlin) - PocketBase Client in Kotlin. ![GitHub Repo stars](https://img.shields.io/github/stars/agrevster/pocketbase-kotlin)
- [Unity (Multiplatform)](https://github.com/Sov3rain/pocketbase-unity) - PocketBase client for Unity 3D game engine. ![GitHub Repo stars](https://img.shields.io/github/stars/Sov3rain/pocketbase-unity)
- [Kotlin (Multiplatform)](https://github.com/IdanAizikNissim/pocketbase-kt) - PocketBase Client in Kotlin. ![GitHub Repo stars](https://img.shields.io/github/stars/IdanAizikNissim/pocketbase-kt)
- [Ruby](https://github.com/azmi2409/pocketbase-ruby) - PocketBase Client in Ruby. ![GitHub Repo stars](https://img.shields.io/github/stars/azmi2409/pocketbase-ruby)

## Self Hosting

- [Coolify PocketBase images](https://github.com/coollabsio/pocketbase) - Unofficial Docker images for ARM and AMD. ![GitHub Repo stars](https://img.shields.io/github/stars/coollabsio/pocketbase)
- [pb-deployer](https://github.com/magooney-loon/pb-deployer) - Automates the lifecycle of deploying PocketBase apps to production ![GitHub Repo stars](https://img.shields.io/github/stars/magooney-loon/pb-deployer)
- [PBLauncher](https://github.com/user0608/pb_launcher) - Manage PocketBase instances — fast, lightweight, open source. ![GitHub Repo stars](https://img.shields.io/github/stars/user0608/pb_launcher)
- [PocketBase on Dokku](https://github.com/blockshiftnetwork/dokku-pocketbase) - Deploy PocketBase instances on Dokku effortlessly. ![GitHub Repo stars](https://img.shields.io/github/stars/blockshiftnetwork/dokku-pocketbase)
- [PocketBase Docker](https://github.com/kdpuvvadi/pocketbase) - Docker images supporting multiple architectures and updated with latest PocketBase releases. ![GitHub Repo stars](https://img.shields.io/github/stars/kdpuvvadi/pocketbase)
- [DigitalOcean](https://github.com/pocketbase/pocketbase/discussions/512) - Guide to deploy in a Droplet.
- [Fly.io](https://github.com/pocketbase/pocketbase/discussions/537) - Guide to deploy for free in Fly.io.
- [Railway](https://github.com/metruzanca/pocketbase_railway) - Guide to deploy on Railway.
- [AWS Lightsail](https://github.com/boustanihani/pocketbase-lightsail-hosting) - Guide to deploy to AWS Lightsail.
- [LocalXpose](https://localxpose.io/docs/tutorials/expose-pocketbase-backend) - Allow public access to a localhost instance.

## TypeScript tools

- [astro-loader-pocketbase](https://github.com/pawcoding/astro-loader-pocketbase) - Astro content loader that reads collections from the PocketBase API. ![GitHub Repo stars](https://img.shields.io/github/stars/pawcoding/astro-loader-pocketbase)
- [pocketbase-query](https://github.com/emresandikci/pocketbase-query) - A TypeScript-based query builder designed to generate complex filter queries for PocketBase. It allows for easy construction of queries using various operators while maintaining a fluent and chainable API. ![GitHub Repo stars](https://img.shields.io/github/stars/emresandikci/pocketbase-query)
- [pocketbase-schema-generator](https://github.com/satohshi/pocketbase-schema-generator) - JS hook for automatically generating schema files. (Zod/TS interfaces) ![GitHub Repo stars](https://img.shields.io/github/stars/satohshi/pocketbase-schema-generator)
- [pb-query](https://github.com/sergio9929/pb-query) - A flexible, strongly-typed query builder with useful helpers to simplify the querying process, featuring examples, documentation, and full autocompletion based on your schema, directly in the IDE. ![GitHub Repo stars](https://img.shields.io/github/stars/sergio9929/pb-query)
- [pocketbase-ts](https://github.com/satohshi/pocketbase-ts) - SDK wrapper with more readable `options` syntax and full type-safety. ![GitHub Repo stars](https://img.shields.io/github/stars/satohshi/pocketbase-ts)
- [pocketbase-jsvm](https://github.com/benallfree/pocketbase-jsvm) - JSVM typings. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/pocketbase-jsvm)
- [pbkit](https://github.com/Karnak19/pbkit) - PocketBase code generation toolkit. Introspect your collections and generate fully typed TypeScript SDKs, with plugins for TanStack Query, Zod, and realtime. ![GitHub Repo stars](https://img.shields.io/github/stars/Karnak19/pbkit)

## SQLite tools

- [Litestream](https://litestream.io/) - Streaming SQLite replication. ![GitHub Repo stars](https://img.shields.io/github/stars/benbjohnson/litestream)
- [Marmot](https://github.com/maxpert/marmot) - A distributed SQLite replicator. ![GitHub Repo stars](https://img.shields.io/github/stars/maxpert/marmot)
- [pocketbase-import](https://github.com/michal-kapala/pocketbase-import) - Import CSV and JSON data into PocketBase collections. ![GitHub Repo stars](https://img.shields.io/github/stars/michal-kapala/pocketbase-import)

## Other tools

- [pb-hooks-dash](https://github.com/deselected/pb-hooks-dash) - Drop-in web dashboard to view and edit PocketBase hooks in the browser. ![GitHub Repo stars](https://img.shields.io/github/stars/deselected/pb-hooks-dash)
- [PocketBaseMobile](https://github.com/rohitsangwan01/pocketbase_mobile) - Android and iOS frameworks for running PocketBase from mobile. ![GitHub Repo stars](https://img.shields.io/github/stars/rohitsangwan01/pocketbase_mobile)
- [pbf](https://github.com/nedpals/pbf) - Library for serializing and deserializing PocketBase filter syntax. ![GitHub Repo stars](https://img.shields.io/github/stars/nedpals/pbf)
- [pb-llm](https://github.com/magooney-loon/pb-llm) - Pocketbase LLM docs scraper ![GitHub Repo stars](https://img.shields.io/github/stars/magooney-loon/pb-llm)
- [PocketBase API Rule Builder](https://pocketbase-api-rule-builder.vercel.app) - A free, open-source web application that makes it easy to generate API rules for PocketBase collections visually. ![GitHub Repo stars](https://img.shields.io/github/stars/kerimovok/pocketbase-api-rule-builder)
- [pocketbase-security-skill](https://github.com/Perufitlife/pocketbase-security-skill) - Open-source MIT auditor that probes anonymously to confirm permissive default-rule wildcards, anonymous record listing exposure, and admin-API misconfigurations. Outputs an HTML report with copy-paste fix snippets. ![GitHub Repo stars](https://img.shields.io/github/stars/Perufitlife/pocketbase-security-skill)
- [PocketBase GPT](https://chatgpt.com/g/g-Owo2FBp4K-pocketbase-gpt) - A GPT that has all of PocketBase's documentation uploaded to it, to give more accurate and up-to-date answers.

## Showcases

- [Beszel](https://beszel.dev) - Lightweight server monitoring with historical data, Docker stats and alerts; its hub is built on PocketBase. ![GitHub Repo stars](https://img.shields.io/github/stars/henrygd/beszel)
- [UpSnap](https://github.com/seriousm4x/UpSnap) - A simple Wake-on-LAN web app written with SvelteKit, Go and PocketBase. ![GitHub Repo stars](https://img.shields.io/github/stars/seriousm4x/UpSnap)
- [wanderer](https://wanderer.to) - Self-hosted trail database for saving and planning hikes. ![GitHub Repo stars](https://img.shields.io/github/stars/open-wanderer/wanderer)
- [CheckCle](https://github.com/operacle/checkcle) - Self-hosted monitoring platform with uptime checks, distributed checks, incident tracking and alerts. ![GitHub Repo stars](https://img.shields.io/github/stars/operacle/checkcle)
- [Primo](https://primo.build) - Builder for client-editable websites, with a PocketBase backend. ![GitHub Repo stars](https://img.shields.io/github/stars/primocms/primo)
- [tinykit](https://tinykit.studio) - Self-hosted AI app builder with a PocketBase realtime database and storage. ![GitHub Repo stars](https://img.shields.io/github/stars/tinykit-studio/tinykit)
- [Dashwise](https://github.com/andreasmolnardev/dashwise) - All-in-one homelab dashboard. ![GitHub Repo stars](https://img.shields.io/github/stars/andreasmolnardev/dashwise)
- [Cially](https://github.com/cially/cially) - Analytics dashboard for Discord servers: member activity, engagement trends and statistics. ![GitHub Repo stars](https://img.shields.io/github/stars/cially/cially)
- [OpenSOHO](https://github.com/rubenbe/opensoho) - OpenWISP alternative for managing a small number of OpenWrt network devices. ![GitHub Repo stars](https://img.shields.io/github/stars/rubenbe/opensoho)
- [Long Habit](https://longhabit.com) - Tracker for long-term habits and recurring tasks, built with PocketBase and React. ![GitHub Repo stars](https://img.shields.io/github/stars/s-petr/longhabit)
- [Canutin](https://canutin.com) - Self-hosted personal finance platform. ![GitHub Repo stars](https://img.shields.io/github/stars/fmaclen/canutin)
- [Realtime Blog](https://github.com/rajesh6161/pbRealtimeBlog) - A React-based realtime blog demo. ![GitHub Repo stars](https://img.shields.io/github/stars/rajesh6161/pbRealtimeBlog)
- [Adnexos](https://github.com/tametsi/adnexos) - Self-hostable expense-splitter on the web. ![GitHub Repo stars](https://img.shields.io/github/stars/tametsi/adnexos)
- [PocketChat](https://github.com/PocketTogether/pocket-chat) - A real-time chat platform built with PocketBase and Vue3, supporting OAuth, notifications, PWA, file/image sharing, permissions, and more. ![GitHub Repo stars](https://img.shields.io/github/stars/PocketTogether/pocket-chat)
- [Facet](https://github.com/jesposito/Facet) - Self-hostable personal profile and portfolio platform built on PocketBase and Svelte, and the open-source core of the [Facet Cloud](https://get-facet.com) creator platform. ![GitHub Repo stars](https://img.shields.io/github/stars/jesposito/Facet)
- [pocketbase-libsql](https://github.com/cobeo2004/pocketbase-libsql) - Scaling Pocketbase with LibSQL and sqld - a Proof Of Concept ![GitHub Repo stars](https://img.shields.io/github/stars/cobeo2004/pocketbase-libsql)
- [Chirkle](https://github.com/border-radius/chirkle) - Ultra-light, self-hosted messenger on a PocketBase server, with federation between instances and lightweight web and Android clients. ![GitHub Repo stars](https://img.shields.io/github/stars/border-radius/chirkle)
- [JustJot](https://justjot.app) - A keyboard-first note-taking full-featured Progressive Web App. [frontend repo](https://github.com/JunoNgx/justjot-frontend) / [backend repo](https://github.com/JunoNgx/justjot-backend) ![GitHub Repo stars](https://img.shields.io/github/stars/JunoNgx/justjot-backend)
- [STJÓRNA](https://github.com/secanis/stjorna) - Multi-tenant product and catalogue management built on PocketBase, with roles, SSO, an S3-backed media library and a read-only REST API for storefronts. ![GitHub Repo stars](https://img.shields.io/github/stars/secanis/stjorna)
- [TinyCld](https://github.com/tinycld) - A full featured workspace with mail/calendar/drive/text/calc package, uses Pocketbase with React Native for realtime db and file storage.  Extends Pocketbase server with golang services for imap/smtp/caldav/webdav.

## Unmaintained

Archived, or no commits in the last two years. They may not work with current PocketBase (v0.23 changed the API).

- [pocketpages 0.x](https://github.com/benallfree/pocketpages) - Server-side EJS pages for PocketBase, npm-based. Archived; v1 is built into PocketOne. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/pocketpages)
- [Vimsnake](https://github.com/patmood/vim_snake) - A realtime WebAssembly game where Vim commands are used as controller inputs. Last commit Aug 2023. ![GitHub Repo stars](https://img.shields.io/github/stars/patmood/vim_snake)
- [SvelteKit Auth](https://github.com/danawoodman/sveltekit-auth-example) - This project is designed as a sample implementation reference for getting authentication setup using SvelteKit. Last commit Dec 2022. ![GitHub Repo stars](https://img.shields.io/github/stars/danawoodman/sveltekit-auth-example)
- [typed-pocketbase](https://github.com/david-plugge/typed-pocketbase) - Generate types from your PocketBase instance and enjoy fully type-safe queries. Last commit Jul 2024. ![GitHub Repo stars](https://img.shields.io/github/stars/david-plugge/typed-pocketbase)
- [PocketNuxt](https://github.com/j-wil/pocket-nuxt) - A Nuxt3 PocketBase starter that builds into a single binary. Last commit Jul 2023. ![GitHub Repo stars](https://img.shields.io/github/stars/j-wil/pocket-nuxt)
- [PocketBase+Litestream example](https://github.com/TylerSustare/pocketbase-framework-litestream) - Template showing Litestream running with PocketBase. Last commit Sep 2022. ![GitHub Repo stars](https://img.shields.io/github/stars/TylerSustare/pocketbase-framework-litestream)
- [PocketBase with Litestream](https://github.com/bscott/pocketbase-litestream/) - Docker example of PocketBase saving/restoring from Litestream. Last commit Sep 2023. ![GitHub Repo stars](https://img.shields.io/github/stars/bscott/pocketbase-litestream)
- [Flutter Chat App](https://github.com/rohitsangwan01/flutter_pocketbase_chat) - A chat app using PocketBase in Flutter. Last commit May 2023. ![GitHub Repo stars](https://img.shields.io/github/stars/rohitsangwan01/flutter_pocketbase_chat)
- [pocketbase-queue](https://github.com/joseferben/pocketbase-queue) - A type-safe queue for background tasks using PocketBase. Last commit Mar 2024. ![GitHub Repo stars](https://img.shields.io/github/stars/joseferben/pocketbase-queue)
- [C# SDK](https://github.com/PRCV1/pocketbase-csharp-sdk) - PocketBase Client in C#. Archived. ![GitHub Repo stars](https://img.shields.io/github/stars/PRCV1/pocketbase-csharp-sdk)
- [PocketBase Drift](https://github.com/rodydavis/pocketbase_drift) - A PocketBase client cached with Drift. Last commit Nov 2024. ![GitHub Repo stars](https://img.shields.io/github/stars/rodydavis/pocketbase_drift)
- [ORM and code generator](https://github.com/iluvadev/PocketBaseClient) - An ORM to manage your PocketBase Application. Last commit Jun 2024. ![GitHub Repo stars](https://img.shields.io/github/stars/iluvadev/PocketBaseClient)
- [PocketBase Next.js App Template](https://github.com/tsensei/nextjs-pocketbase-starter-template) - PocketBase Next.js Template with server & browser client using cookies. Last commit Dec 2023. ![GitHub Repo stars](https://img.shields.io/github/stars/tsensei/nextjs-pocketbase-starter-template)
- [Vue 3 + Vite starter kit](https://github.com/StefanVDWeide/pocketbase-vue) - A starter kit for Vue 3 + Vite + PocketBase. Last commit Nov 2022. ![GitHub Repo stars](https://img.shields.io/github/stars/StefanVDWeide/pocketbase-vue)
- [gobot](https://github.com/benallfree/gobot) - PocketBase as an npm package. CLI and API. Last commit Jul 2024. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/gobot)
- [pb-import](https://github.com/burggraf/pb-import) - Import data from SQLite Databases as well as CSV and TSV files. Last commit Jan 2024. ![GitHub Repo stars](https://img.shields.io/github/stars/burggraf/pb-import)
- [ToDo](https://github.com/rajesh6161/pocketbaseTodo) - React-based To-Do demo app. Last commit Oct 2024. ![GitHub Repo stars](https://img.shields.io/github/stars/rajesh6161/pocketbaseTodo)
- [pb_hooks starter kit](https://github.com/benallfree/ts-pb-hooks-starter) - Build PocketBase JavaScript hooks using TypeScript. Last commit Sep 2023. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/ts-pb-hooks-starter)
- [svelte-query-pocketbase](https://github.com/goknsh/svelte-query-pocketbase) - TanStack Query wrappers around PocketBase for Svelte and SvelteKit that updates the query cache in realtime. Archived. ![GitHub Repo stars](https://img.shields.io/github/stars/goknsh/svelte-query-pocketbase)
- [oAuth](https://github.com/rajesh6161/pocketbase-oauth-demo) - A React-based oAuth demo. Last commit Oct 2022. ![GitHub Repo stars](https://img.shields.io/github/stars/rajesh6161/pocketbase-oauth-demo)
- [Dart Generator](https://github.com/rodydavis/pocketbase_dart_generator) - Generate type safe client SDKs for use in local SQLite, JSON or GraphQL resolvers. Last commit Oct 2023. ![GitHub Repo stars](https://img.shields.io/github/stars/rodydavis/pocketbase_dart_generator)
- [pocketbase-otp](https://github.com/benallfree/pocketbase-otp) - One-Time Passwords for <=v0.22.\*. Last commit Sep 2024. ![GitHub Repo stars](https://img.shields.io/github/stars/benallfree/pocketbase-otp)
- [Quasar starter kit](https://github.com/aaronblondeau/pocketbase_quasar_starter) - Pocketbase with Quasar. Last commit Apr 2023. ![GitHub Repo stars](https://img.shields.io/github/stars/aaronblondeau/pocketbase_quasar_starter)
- [Solid-pocketbase-hooks](https://github.com/kirill-dev-pro/solid-pocketbase-hooks) - Pocketbase hooks for Solid.js. Last commit Feb 2023. ![GitHub Repo stars](https://img.shields.io/github/stars/kirill-dev-pro/solid-pocketbase-hooks)
- [libpb](https://github.com/Hax-io/libpb) - PocketBase client wrapper for D with automatic serialization and deserialization to and from JSON. Last commit Jun 2023. ![GitHub Repo stars](https://img.shields.io/github/stars/Hax-io/libpb)
- [Tutorial](https://studioterabyte.nl/en/blog/pocketbase-vue-3) - Vue 3 tutorial. Companion to the 2022 Vue 3 starter kit.
