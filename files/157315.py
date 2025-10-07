<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="reaun3"/>
        <attribute name="authors" value="windows"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:46:37 PM"/>
        <attribute name="created" value="d2luZG93cztMQVBUT1AtVVVIQTdEMk07MjU2OC0wNy0xNzswMzoxMDoxNiBQTTszMTM2"/>
        <attribute name="edited" value="d2luZG93cztMQVBUT1AtVVVIQTdEMk07MjU2OC0wNy0xNzswMzo0NjozNyBQTTs0OzMyNTk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, n" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i&lt;=n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>