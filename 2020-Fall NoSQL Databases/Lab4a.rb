import 'org.apache.hadoop.hbase.client.HTable'
import 'org.apache.hadoop.hbase.client.Put'

def jbytes( *args )
  args.map { |arg| arg.to_s.to_java_bytes }
end

def put_many( table_name, row, column_values )
    table = HTable.new( @hbase.configuration, table_name )
    p = Put.new( *jbytes( row ) )
    p.add( *jbytes( "text", "", column_values["text:"] ) )
    p.add( *jbytes( "revision", "author", column_values["revision:author"] ) )
    p.add( *jbytes( "revision", "comment", column_values["revision:comment"] ) )
    table.put( p )
    get table_name, row
end

