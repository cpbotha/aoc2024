I am definitely not taking part this year.

This project contains solutions (maybe only 1) in Python and pure Mojo (as far as possible).

## General Mojo

It is unfortunate that the `.magic` environments subdir, 2.5GB and 27900 files (!!) for the default nightly project init, is hardcoded to live under the source dir.

I could work around this with a symlink to a `.magic` dir far outside of this source dir, but something like uv's `UV_PROJECT_ENVIRONMENT` would have been preferable.

## Mojo and VSCode

This is with `mojo 24.6.0.dev2024120105 (78dab9b8)`

VSCode did not pick up my nightly SDK, although I did `magic shell` before invoking vscode from the project directory.

I had to:

```shell
magic shell
echo $MODULAR_HOME
```

then add that directory to `mojo.SDK.additionalSDKs` in the VSCode settings, then invoke "Mojo: Select the default MAX SDK"

With all of this in place, "Run Mojo file" fails with packages failing everywhere, until I do a `magic shell` on the currently active terminal inside vscode. "Debug Mojo file" works more reliably, even without `magic shell` having been invoked.
