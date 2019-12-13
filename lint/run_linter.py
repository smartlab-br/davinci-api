from pylint import epylint as lint

# pylint ./app/**/*.py --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" --reports=n --output-format=parseable
(result, error) = lint.py_run('. --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" --reports=n --output-format=parseable', return_std=True)
# (result, error) = lint.py_run('.')

f = open("./lint/report.txt", "w+")
f.write(result.getvalue())
f.close()