# NCAA Basketball lib

## Introduction

This is a library which scrapes NCAA D2 Basketball game outcomes. It should be easy to modify the code to scrape data for other divisions.

## Installing

To install the library simply copy the `ncaa.py` file to the directory of your Python script. Then simply import it using `import ncaa`.

## Usage

The downloading function can be initiated one of two ways.

### 1.

```ncaa.download(start = "11/4/16", end = "3/24/17")```

where the date is in the format `m/d/y`. This will download all game outcomes from November 4th 2016 to March 24th 2017.

### 2.

```ncaa.download(start = "11/4/16")```

This will download all game outcomes from the start date till the current date.

## Data format

The data returned is in the form of nested lists. Each game is an entry in the returned list. Each of these games is represented by another list where the first entry is the winner of the game.

### Examples

```ncaa.download(start = "11/4/16", end = "3/24/17")[0]```

is the first game found,

```ncaa.download(start = "11/4/16", end = "3/24/17")[0][0]```

is the team that won the first game, and

```ncaa.download(start = "11/4/16", end = "3/24/17")[0][1]```

is the team that lost the first game.
