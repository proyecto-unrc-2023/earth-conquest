from behave import fixture, use_fixture

from app import create_app

@fixture
def empire_client(context, *args, **kwargs):
    app = create_app("testing")
    app.testing = True

    context.client = app.test_client()

    ctx = app.test_request_context()
    ctx.push()

    yield context.client

    ctx.pop()

def before_feature(context, feature):
    # -- HINT: Recreate a new flaskr client before each feature is executed.
    use_fixture(empire_client, context)

def table_to_string(table):
    rows_list = []
    for row in table.rows:
        curr_row = []
        for col in row:
            if col == '':
                curr_row.append('   ')
            elif col == 'B':
                curr_row.append(' B ')
            elif col == 'G':
                curr_row.append(' G ')
            elif col == 'D':
                curr_row.append(' D ')
            elif col == 'TEL':
                curr_row.append(' TEL ')
            elif col == 'K':
                curr_row.append(' K ')
            elif col == 'M':
                curr_row.append(' M ')
            elif col == '2':
                curr_row.append(' 2 ')
            else:
                raise ValueError(f'Unknown cell value: {col}')
        rows_list.append('|'.join(curr_row))
    return '\n'.join(rows_list)
