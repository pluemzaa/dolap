<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 09:36:00 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzowMToyMSBQTTsyNTM2"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzo1OTo1MyBQTTs5OzI2NzA="/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLTNJQ0g4UUk7MjU2OC0wNy0xNzswOTozNjowMCBQTTsyOzI4Nzg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <declare name="Child" type="Integer" array="False" size=""/>
            <input variable="Child"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <declare name="Adult" type="Integer" array="False" size=""/>
            <input variable="Adult"/>
            <declare name="total" type="Integer" array="False" size=""/>
            <assign variable="total" expression="(Child*120)+(Adult*189)"/>
            <output expression="&quot;You ordered &quot;&amp;Child&amp;&quot; children and &quot;&amp;Adult&amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>