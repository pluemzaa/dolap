<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="eahaerhaer"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 05:12:10 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtVUYzQlNVRDM7MjU2OC0wNy0xNjswNDowNTowMyBQTTsyNzc0"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtVUYzQlNVRDM7MjU2OC0wNy0xNjswNToxMjoxMCBQTTs1OzI4ODM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Child" type="Integer" array="False" size=""/>
            <declare name="ad" type="Integer" array="False" size=""/>
            <declare name="total" type="Integer" array="False" size=""/>
            <output expression="&quot;price List:&quot;" newline="True"/>
            <output expression="&quot;-Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;-Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="child"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="ad"/>
            <assign variable="total" expression="(child*120)+(ad*189)"/>
            <output expression="&quot;You ordered  &quot; &amp; (child) &amp; &quot; children and&quot; &amp; (ad) &amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp; (total) &amp; &quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>