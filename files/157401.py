<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="33333333"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 12:31:39 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xODsxMjowNjoyOSBQTTsyNTUw"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xODsxMjozMTozOSBQTTsxOzI2NTc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="ns, ne, pp" type="Integer" array="False" size=""/>
            <assign variable="pp" expression="0"/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="ns"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="ne"/>
            <while expression="ns&lt;=ne">
                <output expression="&quot;&quot;&amp;ns" newline="True"/>
                <assign variable="ns" expression="ns+1"/>
            </while>
        </body>
    </function>
</flowgorithm>