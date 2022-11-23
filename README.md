# Grafolo49

A GraphQL app for Loto6.49

## Install venv and dependencies

### Venv

`python3 -m venv grafolo49`

`source venv/bin/activate` or `venv/Scripts/activate.bat`

### Dependencies

`pip install -r requirements.txt`

## Run project

To tell Flask where to start :
`export FLASK_APP=app.py`

And then `flask run`, you should have app running on [localhost](127.0.0.1:5000).

## How to use

Access the app on [http://localhost:5000/graphql](http://localhost:5000/graphql) and then, you can search draws as 

```graphql
query AllDraws {
  listDraws {
    success
    errors
    draw {
      draw_date
      number_1
      number_c
    }
  }
}
```

It is possible to limit the results by adding the parameter `limit` and to order by date with `ordered` boolean parameter:

```graphql
query AllDraws {
  listDraws(limit: 2, ordered: true) {
    success
    errors
    draw {
      draw_date
      number_1
      number_c
    }
  }
}
```

By default, `limit` parameter is set to 10 and results are ordered by date (most recent draws first).