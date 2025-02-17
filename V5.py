import re
def text_extraction(file_name):
    with open(file_name,'r') as f:
        raw_text=f.read()
    return raw_text
def query_extraction(txt):
    pattern=r'(SQL_QUERY\()([\s\S]*)(\)\s*END_QUERY)'
    mat=re.search(pattern,txt)
    query=mat.group(2)
    return query
def schema_name_change(text,sch):
    pattern=r'(FROM\s*|INNER JOIN\s*)(\(*)(\"\w+\"\s)+'
    def add_schema(match):
        prefix=match.group(1)
        parantheses=match.group(2)if match.group(2) else ''
        table=match.group(3)
        table_name=table.replace('''"''','')
        return prefix+parantheses+sch+"."+table_name
    return re.sub(pattern,add_schema,text)
def replace_query(updated_query,text):
    pattern=r'(SQL_QUERY\()([\s\S]*)(\)\s*END_QUERY)'
    def replaced_query(match):
        grp1=match.group(1)
        grp2=match.group(2)
        grp3=match.group(3)
        return grp1+updated_query+grp3
    return re.sub(pattern,replaced_query,text)
def access_replacement(txt,datasource_name,database_name,Dynamic_file):
    pattern=r'ACCESSDATA64 CONNECTOR NAME "([^"]+)" USER "([^"]+)" PASSWORD (\d+) TO "([^"]+)" CHARMAX (\d+) MEMOMAX (\d+)'
    replacement=f'''ACCESSDATA64 ODBC "{datasource_name}" NAME {database_name} TO "{Dynamic_file}" CHARMAX 5000 MEMOMAX 10000'''
    return re.sub(pattern,replacement,txt)
def source_replacement(txt):
    pattern = r'SOURCE\([^\)]*\)'
    replacement='SOURCE()'
    return re.sub(pattern,replacement,txt)
def query_generator(txt,file_name):
    with open(f'converted-{file_name}.txt','w') as f:
        f.write(txt)
file_name="24 before.txt"
raw_text=text_extraction(file_name)
old_query=query_extraction(raw_text)
schema_updated=schema_name_change(old_query,'prpd_gold.a3s_rt')
replaced_queries=replace_query(schema_updated,raw_text)
access_line=access_replacement(replaced_queries,'Dsn','DATABRICKS_ABHFL_SIMBA','%V_INT%MASTER2_data_bricks_0001.FIL')
source_line=source_replacement(access_line)
query_generator(source_line,file_name)



