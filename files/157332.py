<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="j2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 04:00:46 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzo0NjozMSBQTTsyNTQ2"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswNDowMDo0NiBQTTsxOzI2NTE="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="nn, n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="n"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="nn"/>
            <output expression="n" newline="True"/>
            <while expression="n &lt; nn">
                <output expression="(n+1)" newline="True"/>
                <assign variable="n" expression="n + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>