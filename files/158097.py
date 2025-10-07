<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test9_lap4"/>
        <attribute name="authors" value="NATNICHA-PC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-21 05:57:59 PM"/>
        <attribute name="created" value="TkFUTklDSEEtUEM7TkFUTklDSEE7MjAyNS0wNy0yMTswNTo0NzoxNiBQTTsyNjQy"/>
        <attribute name="edited" value="TkFUTklDSEEtUEM7TkFUTklDSEE7MjAyNS0wNy0yMTswNTo1Nzo1OSBQTTsxOzI3NTg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, n" type="Integer" array="False" size=""/>
            <output expression="&quot;input start number:&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;input end number:&quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i&lt;=n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>