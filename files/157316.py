<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:46:04 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzowNToyNyBQTTsyNTQ2"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzo0NjowNCBQTTsxOzI2NTQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="total" type="Real" array="False" size=""/>
            <declare name="Child, Adult" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="child"/>
            <input variable="Adult"/>
            <assign variable="total" expression="(child* 120) + (adult * 189)"/>
            <output expression="&quot;You ordered &quot;&amp;child&amp;&quot; children and  &quot;&amp;Adult&amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price:&quot;&amp;total&amp;&quot;  Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>