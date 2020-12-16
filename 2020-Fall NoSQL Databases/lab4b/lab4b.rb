#Your Jruby script code goes here

require 'time'
import 'org.apache.hadoop.hbase.client.HTable'
import 'org.apache.hadoop.hbase.client.Put'
import 'javax.xml.stream.XMLStreamConstants'

def jbytes( *args )
    args.map { |arg| String(arg.to_s).to_java_bytes }
end

factory = javax.xml.stream.XMLInputFactory.newInstance
reader = factory.createXMLStreamReader(java.lang.System.in)

document = nil
buffer = nil
count = 0

table = HTable.new( @hbase.configuration, 'foods' )
table.setAutoFlush( false )

while reader.has_next
    type = reader.next
    if type == XMLStreamConstants::START_ELEMENT
        case reader.local_name
        when 'Food_Display_Row' then document = {}
        when /Food_Code|Display_Name|Portion_Default|Portion_Amount|Portion_Display_Name|Factor|Increment|Multiplier
            |Grains|Whole_Grains|Vegetables|Orange_Vegetables|Drkgreen_Vegetables|Starchy_vegetables|Other_Vegetables
            |Fruits|Milk|Meats|Soy|Drybeans_Peas|Oils|Solid_Fats|Added_Sugars|Alcohol|Calories|Saturated_Fats/ then buffer = []
        end
    elsif type == XMLStreamConstants::CHARACTERS
        buffer << reader.text unless buffer.nil?
    elsif type == XMLStreamConstants::END_ELEMENT
        case reader.local_name
        when /Food_Code|Display_Name|Portion_Default|Portion_Amount|Portion_Display_Name|Factor|Increment|Multiplier
            |Grains|Whole_Grains|Vegetables|Orange_Vegetables|Drkgreen_Vegetables|Starchy_vegetables|Other_Vegetables
            |Fruits|Milk|Meats|Soy|Drybeans_Peas|Oils|Solid_Fats|Added_Sugars|Alcohol|Calories|Saturated_Fats/
            document[reader.local_name] = buffer.join
        when 'Food_Display_Row'
            key = document['Food_Code'].to_s.to_java_bytes
            # ts = ( Time.now ).to_i
            # p = Put.new( key, ts )
            p = Put.new( key )
            p.add( *jbytes( "name", "", document['Display_Name'] ) )
            p.add( *jbytes( "fact", "Portion_Default"      , document['Portion_Default'] ) )       #Portion_Default
            p.add( *jbytes( "fact", "Portion_Amount"       , document['Portion_Amount'] ) )        #Portion_Amount  
            p.add( *jbytes( "fact", "Portion_Display_Name" , document['Portion_Display_Name'] ) )  #Portion_Display_Name  
            p.add( *jbytes( "fact", "Factor"               , document['Factor'] ) )                #Factor  
            p.add( *jbytes( "fact", "Increment"            , document['Increment'] ) )             #Increment  
            p.add( *jbytes( "fact", "Multiplier"           , document['Multiplier'] ) )            #Multiplier
            p.add( *jbytes( "fact", "Grains"               , document['Grains'] ) )                #Grains  
            p.add( *jbytes( "fact", "Whole_Grains"         , document['Whole_Grains'] ) )          #Whole_Grains  
            p.add( *jbytes( "fact", "Vegetables"           , document['Vegetables'] ) )            #Vegetables  
            p.add( *jbytes( "fact", "Orange_Vegetables"    , document['Orange_Vegetables'] ) )     #Orange_Vegetables  
            p.add( *jbytes( "fact", "Drkgreen_Vegetables"  , document['Drkgreen_Vegetables'] ) )   #Drkgreen_Vegetables  
            p.add( *jbytes( "fact", "Starchy_vegetables"   , document['Starchy_vegetables'] ) )    #Starchy_vegetables  
            p.add( *jbytes( "fact", "Other_Vegetables"     , document['Other_Vegetables'] ) )      #Other_Vegetables  
            p.add( *jbytes( "fact", "Fruits"               , document['Fruits'] ) )                #Fruits  
            p.add( *jbytes( "fact", "Milk"                 , document['Milk'] ) )                  #Milk  
            p.add( *jbytes( "fact", "Meats"                , document['Meats'] ) )                 #Meats  
            p.add( *jbytes( "fact", "Soy"                  , document['Soy'] ) )                   #Soy  
            p.add( *jbytes( "fact", "Drybeans_Peas"        , document['Drybeans_Peas'] ) )         #Drybeans_Peas  
            p.add( *jbytes( "fact", "Oils"                 , document['Oils'] ) )                  #Oils  
            p.add( *jbytes( "fact", "Solid_Fats"           , document['Solid_Fats'] ) )            #Solid_Fats
            p.add( *jbytes( "fact", "Added_Sugars"         , document['Added_Sugars'] ) )          #Added_Sugars
            p.add( *jbytes( "fact", "Alcohol"              , document['Alcohol'] ) )               #Alcohol  
            p.add( *jbytes( "fact", "Calories"             , document['Calories'] ) )              #Calories
            p.add( *jbytes( "fact", "Saturated_Fats"       , document['Saturated_Fats'] ) )        #Saturated_Fats
            table.put( p )
            count += 1
            table.flushCommits() if count % 10 == 0
            if count % 500 == 0
                puts "#{count} records inserted (#{document['title']})"
            end
        end
    end
end
table.flushCommits()

#Do not remove the exit call below
exit

# <page>
# <title>Lie Like This</title>
# <ns>0</ns>
# <id>65475910</id>
# <redirect title="Julia Michaels discography" />
# <revision>
#   <id>981434181</id>
#   <timestamp>2020-10-02T08:45:44Z</timestamp>
#   <contributor>
#     <username>AshMusique</username>
#     <id>34898467</id>
#   </contributor>
#   <comment>[[WP:AES|←]]Redirected page to [[Julia Michaels discography]]</comment>
#   <model>wikitext</model>
#   <format>text/x-wiki</format>
#   <text bytes="40" xml:space="preserve">#REDIRECT [[Julia Michaels discography]]</text>
#   <sha1>49x81xypba6z0iovioii4f9vu8s6bjz</sha1>
# </revision>
# </page>